from django import forms
from .models import Category, Service


class CategoryCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Название категории')
    weight = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'min': '0'
    }), label='Приоритет')

    class Meta:
        model = Category
        fields = ('title', 'weight',)


class ServiceCreateForm(forms.ModelForm):
        
    def __init__(self, enterprise, *args, **kwargs):
        super(ServiceCreateForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Category.objects.filter(enterprise=enterprise)
    
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Услуга')
    service_desc = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}), label='Короткое описание')
    service_duration = forms.DurationField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))
    min_price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ), label='Минимальная цена')
    max_price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control'}
    ), label='Максимальная цена')
    access = forms.BooleanField(widget=forms.CheckboxInput, label='Доступен для записи')

    class Meta:
        model = Service
        fields = ('title', 'service_desc', 'service_duration', 'min_price', 'max_price', 'access', 'service')
