from django import forms

from profile.models import ClientProfile
from service.models import Service
from employee.models import Employee
from .models import Event

client_select = ClientProfile.objects.all()
service_select = Service.objects.all()
staff_select = Employee.objects.all()


class EventForm(forms.ModelForm):
    service = forms.ModelChoiceField(service_select, widget=forms.Select(attrs={'class': 'chosen-select'}))
    staff = forms.ModelChoiceField(staff_select, widget=forms.Select(attrs={'class': 'chosen-select'}))
    client = forms.ModelChoiceField(client_select, widget=forms.Select(attrs={'class': 'chosen-select'}))
    start_event = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Event
        fields = ('service', 'staff', 'start_event', 'client',)
