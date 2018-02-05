from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import ClientProfile

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
        fields = ('username', 'email', )

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
