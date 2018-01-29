from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Employee
from .forms import EmployeeForm


# Create your views here.

@login_required
def employee(request):
    employees = Employee.objects.filter(enterprise__owner=request.user)
    template_name = 'employee/list.html'
    template_data = {'employees': employees}
    return render(request, template_name, template_data)


@login_required
def new_employee(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)
    template_name = 'employee/new_employee.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)
