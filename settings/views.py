from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from enterprise.models import Enterprise
from enterprise.forms import (
    EnterpriseCreateForm,
    EnterpriseUpdateForm,
    EnterpriseUpdateContactForm,
    EnterpriseUpdateScheduleForm
)

from employee.models import Employee
from employee.forms import EmployeeForm

from service.models import Category, Service
from service.forms import CategoryCreateForm, ServiceCreateForm


# Write you views here

@login_required
def enterprise_update(request):
    instance = Enterprise.objects.get(owner=request.user)
    if request.POST:
        form = EnterpriseCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            update_data = form.cleaned_data
            Enterprise.objects.filter(owner=request.user).update(**update_data)
            return HttpResponseRedirect('/')
    else:
        form = EnterpriseCreateForm(instance=instance)
    template_name = 'settings/enterprise/enterprise_update.html'
    template_data = {
        'instance': instance,
        'form': form,
    }
    return render(request, template_name, template_data)


@login_required
def personal(request):
    user = request.user
    enterprise = Enterprise.objects.get(owner=request.user)
    employee = Employee.objects.filter(enterprise=enterprise)
    if request.POST:
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form_data = form.cleaned_data
            new_staff = Employee.objects.create(enterprise=enterprise, **form_data)
            new_staff.save()
            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm(request.POST or None)
    template_name = 'settings/staff/personal.html'
    template_data = {'employee': employee, 'form': form}
    return render(request, template_name, template_data)


@login_required
def personal_detail(request, pk):
    instance = Employee.objects.get(pk=pk)
    template_name = 'settings/staff/staff-detail.html'
    template_data = {'instance': instance}
    return render(request, template_name, template_data)


@login_required
def service(request, pk):
    user = request.user
    category = Category.objects.filter(enterprise__owner=user)
    services = Service.objects.filter(service=category)
    template_name = 'settings/service/service_group.html'
    template_data = {'category': category, 'service': services}
    return render(request, template_name, template_data)


@login_required
def new_category(request, pk):
    instance = Enterprise.objects.get(pk=pk)
    if request.POST:
        form = CategoryCreateForm(request.POST or None)
        if form.is_valid():
            post_data = form.cleaned_data
            Category.objects.get_or_create(enterprise=instance, **post_data)
            return HttpResponseRedirect(reverse('settings:service-group', kwargs={'pk': instance.pk}))
    else:
        form = CategoryCreateForm()
    template_name = 'settings/service/new_category.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)


@login_required
def new_service(request):
    enterprise = Enterprise.objects.get(owner=request.user)
    if request.POST:
        form = ServiceCreateForm(request.POST or None)
        if form.is_valid():
            post_data = form.cleaned_data
            Service.objects.create(enterprise=enterprise, **post_data)
            return HttpResponseRedirect(reverse("settings:service-group", kwargs={'pk': enterprise.pk}))
    else:
        form = ServiceCreateForm()
    template_name = 'settings/service/new_service.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)
