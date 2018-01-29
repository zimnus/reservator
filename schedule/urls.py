from django.conf.urls import url

from .views import schedule, get_schedule_list

urlpatterns = [
    url(r'^timetable/(?P<company_id>[\w-]+)/$', schedule, name='schedule'),
    url(r'^get_schedule_list/(?P<date>[\w-]+)/$', get_schedule_list, name="get-schedule-list"),
]
