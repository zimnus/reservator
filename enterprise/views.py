from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Enterprise, WORK_DAYS
from .forms import EnterpriseCreateForm
from employee.forms import EmployeeForm
from account.models import ClientProfile
from django.contrib.auth.decorators import permission_required


# Create your views here.

########### NEW CODE #################

def enterprise_list(request):
    query = request.GET.get('q')
    if query:
        object_list = Enterprise.objects.all().search(query)
        # object_list = Enterprise.objects.filter(name__iexact=query)
    else:
        object_list = Enterprise.objects.all()
    work_days = WORK_DAYS
    template_name = 'enterprise/enterprise_list.html'
    template_data = {'object_list': object_list, 'work_days': work_days}
    return render(request, template_name, template_data)


def enterprise_detail(request, pk):
    instance = Enterprise.objects.get(pk=pk)
    employee_list = Enterprise.objects.employee_list(pk=pk)
    template_name = 'enterprise/enterprise_detail.html'
    template_data = {'instance': instance, 'employee_list': employee_list}
    return render(request, template_name, template_data)


@login_required
@permission_required('user.enterprise_create', login_url='/')
def create_enterprise(request):
    profile = ClientProfile.objects.get(user=request.user)
    if request.POST:
        form = EnterpriseCreateForm(request.POST or None)
        if form.is_valid():
            new_enterprise = form.save(commit=False)
            new_enterprise.profile = profile
            new_enterprise.save()
            return HttpResponseRedirect('/')
    else:
        form = EnterpriseCreateForm()
    template_name = 'enterprise/create.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)


@login_required
@permission_required('user.employee_add', login_url='/')
def register_employee(request, pk):
    if request.POST:
        form = EmployeeForm(request.POST or None)
        if form.is_valid():
            new_employee = form.save(commit=False)
            new_employee.enterprise = Enterprise.objects.get(pk=pk)
            new_employee.save()
            return HttpResponseRedirect('/')
    else:
        form = EmployeeForm()
    template_name = 'enterprise/include_employee.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)
