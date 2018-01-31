from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = (
            'show_rating',
            'rating',
            'votes_count',
            'hidden',
            'fired',
        )
