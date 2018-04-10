from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from reservator.decorators import manager_required
from enterprise.models import Enterprise
from employee.models import Employee
from event.models import Event
from event.forms import EventForm
from schedule.models import StaffSchedule


# Create your views here.


# All staff
@manager_required
def schedule(request):
    event_form = EventForm(request.POST or None)
    enterprise = Enterprise.objects.get(owner=request.user)
    schedules = StaffSchedule.objects.filter(staff__enterprise=enterprise)
    template_name = 'schedule/schedules.html'
    template_data = {'schedules': schedules, 'event_form': event_form}
    return render(request, template_name, template_data)


# Single staff
@manager_required
def staff_schedule(request, staff_pk):
    instance = Employee.objects.get(pk=staff_pk)
    template_name = 'schedule/staff_timetable.html'
    template_data = {'instance': instance}
    return render(request, template_name, template_data)


@manager_required
def staff_new_event(request):
    form = EventForm(request.POST or None)
    template_name = 'schedule/staff_new_event.html'
    template_data ={'form': form}
    return render(request, template_name, template_data)