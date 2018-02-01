from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from enterprise.models import Enterprise
from enterprise.forms import EnterpriseUpdateForm

from service.models import Category, Service
from service.forms import ServiceCreateForm


# Write you views here

def base(request):
    enterprises = Enterprise.objects.filter(owner=request.user)
    template_name = 'settings/enterprise_base.html'
    template_data = {'enterprises': enterprises}
    return render(request, template_name, template_data)


def base_edit(request, pk):
    instance = Enterprise.objects.get(pk=pk)

    if request.POST:
        form = EnterpriseUpdateForm(request.POST or None)
        if form.is_valid():
            update_data = form.cleaned_data
            Enterprise.objects.filter(pk=instance.id).update(**update_data)
            return HttpResponseRedirect('/')
    else:
        form = EnterpriseUpdateForm(initial=model_to_dict(instance))
    template_name = 'settings/enterprise_update.html'
    template_data = {'instance': instance, 'form': form}
    return render(request, template_name, template_data)


def personal(request):
    pass


def service(request, pk):
    instance = Category.objects.filter(enterprise=pk)
    template_name = 'settings/service_group.html'
    template_data = {'instance': instance}
    return render(request, template_name, template_data)
