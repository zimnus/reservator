from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

from .models import Enterprise
from .forms import EnterpriseCreateForm, EnterpriseUpdateForm
from service.models import Category, Service
from employee.models import Employee
from account.models import ClientProfile
from django.contrib.auth.decorators import permission_required


# Create your views here.

########### NEW CODE #################

@login_required
def dashboard(request):
    template_name = 'enterprise/dashboard.html'
    template_data = {}
    return render(request, template_name, template_data)


@login_required
def enterprise(request):
    enterprises = Enterprise.objects.get_list(request.user)
    template_name = 'enterprise/enterprise_list.html'
    template_data = {'enterprises': enterprises}
    return render(request, template_name, template_data)


@login_required
def detail(request, pk):
    instance = Enterprise.objects.get(pk=pk)
    category = Category.objects.filter(enterprise=instance)
    service = Service.objects.filter(service__enterprise=instance)
    employees = Employee.objects.filter(enterprise=pk)
    template_name = 'enterprise/enterprise_detail.html'
    template_data = {
        'instance': instance,
        'category': category,
        'service': service,
        'employees': employees
    }
    return render(request, template_name, template_data)


@login_required
def create(request):
    if request.POST and request.FILES:
        form = EnterpriseCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_enterprise = form.save(commit=False)
            new_enterprise.owner = request.user
            new_enterprise.save()
            return HttpResponseRedirect('/')
    else:
        form = EnterpriseCreateForm()
    template_name = 'enterprise/create.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)


@login_required
def update(request, pk):
    instance = Enterprise.objects.get(pk=pk)

    if request.POST:
        form = EnterpriseUpdateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            update_data = form.cleaned_data
            Enterprise.objects.filter(pk=instance.id).update(**update_data)
            return HttpResponseRedirect('/')
    else:
        form = EnterpriseUpdateForm(initial=model_to_dict(instance))
    template_name = 'enterprise/enterprise_update.html'
    template_data = {'instance': instance, 'form': form}
    return render(request, template_name, template_data)
