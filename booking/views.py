from django.shortcuts import render
from django.http import HttpResponseRedirect

from enterprise.models import Enterprise
from employee.models import Employee
from .models import OnlineBooking
from .forms import BookingForms


# Create your views here.


def record(request, enterprise_pk, employee_pk):
    enterprise = Enterprise.objects.get(pk=enterprise_pk)
    employee = Employee.objects.get(pk=employee_pk)
    if request.POST:
        form = BookingForms(request.POST or None)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.enterprise = enterprise
            new_record.executor = employee
            new_record.save()
            return HttpResponseRedirect('/')
    else:
        form = BookingForms()
    template_data = {'form': form}
    template_name = 'booking/record.html'
    return render(request, template_name, template_data)


def booking_list(request, enterprise):
    active_list = OnlineBooking.objects.active(enterprise)
    complete_list = OnlineBooking.objects.complete(enterprise)
    template_data = {'active_list': active_list, 'complete_list': complete_list}
    template_name = 'booking/list.html'
    return render(request, template_name, template_data)
