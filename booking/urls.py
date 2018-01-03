from django.conf.urls import url

from .views import record, booking_list

urlpatterns = [
    url(r'^record/(?P<enterprise_pk>[\w-]+)/(?P<employee_pk>[\w-]+)/$', record, name='record'),
    url(r'^list/(?P<enterprise>[\w-]+)/$', booking_list, name='list'),
]