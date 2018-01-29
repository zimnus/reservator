from django import forms

from .models import Enterprise


class EnterpriseCreateForm(forms.ModelForm):

    class Meta:
        model = Enterprise
        exclude = ('owner', 'active_stuff_count', )