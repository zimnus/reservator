from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from enterprise.models import Enterprise
from employee.models import Employee
from event.models import Event
from event.forms import EventForm
from .models import StaffSchedule


# Create your views here.

@login_required
def schedule(request):
    event_form = EventForm(request.POST or None)
    enterprise = Enterprise.objects.get(owner=request.user)
    try:
        schedules = StaffSchedule.objects.filter(staff__enterprise=enterprise)
    except StaffSchedule.DoesNotExist:
        schedules = None
    template_name = 'schedule/schedules.html'
    template_data = {'schedules': schedules, 'event_form': event_form}
    return render(request, template_name, template_data)


def get_schedule_list(request, date):
    user = request.user
    schedules = StaffSchedule.objects.filter(staff__enterprise__owner=user).filter(work_date=date)
    employee = []
    for staff in schedules:
        employee.append(staff.staff.name)
    events = Event.objects.filter(enterprise__owner=user).filter(start_event__icontains=date)
    print("Events: \n", events)
    template_data = {
        'staff': list(schedules.values()),
        'events': list(events.values()),
        'employee': employee
    }
    return JsonResponse(template_data)

