from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from reservator.decorators import manager_required

from event.models import Event
from enterprise.models import Enterprise
from enterprise.forms import (
    EnterpriseCreateForm,
    EnterpriseUpdateForm,
    EnterpriseUpdateLogoForm,
    EnterpriseUpdateContactForm,
    EnterpriseUpdateScheduleForm
)

from employee.models import Employee
from employee.forms import EmployeeForm

from service.models import Category, Service
from service.forms import CategoryCreateForm, ServiceCreateForm


# Write you views here

@manager_required
def enterprise_update(request, pk):
    instance = Enterprise.objects.get(pk=pk)
    logo_form = EnterpriseUpdateLogoForm(initial=model_to_dict(instance))
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
        'logo_form': logo_form,
    }
    return render(request, template_name, template_data)


@require_POST
def update_logo(request, pk):
    form = EnterpriseUpdateLogoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        update_data = form.cleaned_data
        print('Form data \n', update_data)
        Enterprise.objects.filter(pk=pk).update(**update_data)
        return HttpResponseRedirect('/')


@manager_required
def personal(request, pk):
    enterprise = Enterprise.objects.get(pk=pk)
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


@manager_required
def personal_detail(request, pk):
    instance = Employee.objects.get(pk=pk)
    events = Event.objects.filter(staff=instance)
    template_name = 'settings/staff/staff-detail.html'
    template_data = {'instance': instance, 'events': events}
    return render(request, template_name, template_data)


@manager_required
def service(request, pk):
    user = request.user
    category = Category.objects.filter(enterprise__owner=user)
    services = Service.objects.filter(service=category)
    template_name = 'settings/service/service_group.html'
    template_data = {'category': category, 'service': services}
    return render(request, template_name, template_data)


@manager_required
def new_category(request, pk):
    user = request.user
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


@manager_required
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
