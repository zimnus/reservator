from django import forms
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from .models import Enterprise, City


class EnterpriseCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'summernote'}), label='Описание')

    class Meta:
        model = Enterprise
        exclude = ('owner', 'active_stuff_count',)


class EnterpriseUpdateScheduleForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ('schedule', )


class EnterpriseUpdateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Название')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'summernote'}), label='Описание')

    # def __init__(self, *args, **kwargs):
    #     super(EnterpriseUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.all()


class EnterpriseUpdateContactForm(forms.Form):
    city = forms.ModelChoiceField(City.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),
                                  label="Город")
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Адрес")
    phone = forms.CharField(widget=PhoneNumberInternationalFallbackWidget(attrs={
        'class': 'form-control',
        'data-mask': '+38 (999) 999-99-99'
    }), label="Контактный телефон")


class EnterpriseUpdateLogoForm(forms.Form):
    logo = forms.ImageField()
