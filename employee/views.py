from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Employee
from .forms import EmployeeForm
from enterprise.models import Enterprise


# Create your views here.

@login_required
def employee(request):
    enterprises = Enterprise.objects.filter(owner=request.user)
    employees = Employee.objects.filter(enterprise__owner=request.user)
    template_name = 'employee/list.html'
    template_data = {'enterprises': enterprises, 'employees': employees}
    return render(request, template_name, template_data)


@login_required
def new_employee(request):
    if request.POST and request.FILES:
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            HttpResponseRedirect(reverse('employee:employee'))
    else:
        form = EmployeeForm()
    template_name = 'employee/new_employee.html'
    template_data = {'form': form}
    return render(request, template_name, template_data)
