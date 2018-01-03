from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    start = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))
    end = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))

    class Meta:
        model = Employee
        exclude = ('enterprise',)
