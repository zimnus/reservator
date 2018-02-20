from django.conf.urls import url

from .views import schedule

urlpatterns = [
    url(r'^timetable/$', schedule, name='schedule'),
]
