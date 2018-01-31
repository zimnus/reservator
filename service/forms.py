from django import forms
from .models import Service


class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        labels = {
            'title': 'Услуга',
            'service_desc': 'Короткое описание',
            'service_duration': 'Длительность услуги',
            'min_price': 'Минимальная цена',
            'max_price': 'Максимальная цена',
            'service': 'Категория',
            'staff': 'Сотрудники',
        }

    def __init__(self, *args, **kwargs):
        super(ServiceCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['service_desc'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['service_duration'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['min_price'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['max_price'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['service'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['staff'].widget.attrs.update({
            'class': 'form-control dual_select',
            'multiple': 'true'
        })
