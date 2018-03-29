from django.conf.urls import url

from .views import schedule, staff_schedule

urlpatterns = [
    url(r'^timetable/$', schedule, name='schedule'),
    url(r'^timetable/(?P<staff_pk>[\w-]+)$', staff_schedule, name='staff-schedule'),
]
