from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from .utils import generate_username

from .models import ClientProfile
from enterprise.models import Enterprise

from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

User = get_user_model()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'login'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email already use")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password must be match")
        return password2


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        exclude = ('user',)


class ClientCreateForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self):
        try:
            new_user = get_user_model().objects.get(email__iexact=self.cleaned_data['email'])
            password = None
        except get_user_model().DoesNotExist:
            password = get_user_model().objects.make_random_password()
            new_user = get_user_model().objects.create_user(
                username=generate_username(),
                password=password,
                first_name=self.cleaned_data.get('name', ''),
                last_name=self.cleaned_data.get('last_name', ''),
                email=self.cleaned_data.get('email', ''),
                client=True
            )
        print("User login: \t", new_user.username)
        print("User generate password: \t", password)
        ClientProfile.create(
            new_user,
            password
        )


class EnterpriseManagerForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    phone = forms.CharField(widget=PhoneNumberInternationalFallbackWidget(attrs={
        'class': 'form-control',
        'data-mask': '+38 (999) 999-99-99'
    }), label="Контактный телефон")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(EnterpriseManagerForm, self).__init__(*args, **kwargs)

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password and password2 and password != password2:
            raise ValidationError('Password must be confirm!')
        return password2

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = get_user_model().objects.filter(username__iexact=username)
        if qs.exists():
            raise ValidationError('This username already exists!')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = get_user_model().objects.filter(email__iexact=email)
        if qs.exists():
            raise ValidationError('This email already exists!')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        qs = get_user_model().objects.filter(phone__iexact=phone)
        if qs.exists():
            raise ValidationError('This email already exists!')
        return phone

    def save(self):
        username = self.cleaned_data.get('username', '')
        email = self.cleaned_data.get('email', '')
        phone = self.cleaned_data.get('phone', '')
        password = self.cleaned_data.get('password', '')
        manager = True
        new_user = get_user_model().objects.create_user(username=username, phone=phone, email=email, manager=manager)
        new_user.set_password(password)
        new_user.save()
        Enterprise.objects.create(owner=new_user)
