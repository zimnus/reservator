from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from enterprise.models import Enterprise
from employee.models import Employee
from .models import StaffSchedule


# Create your views here.

@login_required
def schedule(request, company_id):
    try:
        schedules = StaffSchedule.objects.filter(staff__enterprise=company_id)
    except StaffSchedule.DoesNotExist:
        schedules = None
    template_name = 'schedule/schedules.html'
    template_data = {'schedules': schedules}
    return render(request, template_name, template_data)


def get_schedule_list(request):
    schedules = StaffSchedule.objects.filter()
    for s in schedules:
        print("Staff: \t{}\nWork date:\t{}\nIs work:\t{}\nSchedule:\t{}".format(s.staff.name, s.work_date, s.is_work, s.schedule))
        print("*"*100)
    template_data = {
        'staff': list(schedules.values()),
        # 'schedules': schedules.schedule
    }
    return JsonResponse(template_data)
