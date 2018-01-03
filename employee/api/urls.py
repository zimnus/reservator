from django.conf.urls import url

from .views import (
    EmployeeAPIView,
    EmployeeAPIDetailView
)

urlpatterns = [
    url(r'^$', EmployeeAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', EmployeeAPIDetailView.as_view(), name='detail'),
]
