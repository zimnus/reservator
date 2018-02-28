from enterprise.models import Enterprise
from django.shortcuts import HttpResponseRedirect


def enterprise(request):
    user = request.user
    if user.is_anonymous:
        return {'enterprise': None}
    try:
        qs = Enterprise.objects.get(owner=user)
        return {'enterprise': qs}
    except Enterprise.DoesNotExist:
        return {'enterprise': None}