from django import forms
from employee.models import Employee, Position
from service.models import Service


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя')
    specialization = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Специализация')
    weight = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
                                label='Приоритет')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email')
    information = forms.CharField(widget=forms.Textarea(attrs={'class': 'summernote'}), label='Описание')

    class Meta:
        model = Employee
        exclude = (
            'enterprise',
            'show_rating',
            'rating',
            'votes_count',
            'hidden',
            'fired',
        )

    def __init__(self, enterprise, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['staff'].queryset = Service.objects.filter(enterprise=enterprise)
        self.fields['position'].queryset = Position.objects.filter(enterprise=enterprise)
