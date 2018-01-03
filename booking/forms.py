from django import forms

from .models import OnlineBooking


class BookingForms(forms.ModelForm):

    class Meta:
        model = OnlineBooking
        exclude = ('enterprise', 'executor', 'status', )