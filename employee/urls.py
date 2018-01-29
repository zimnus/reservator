from django.conf.urls import url

from .views import (
    employee,
    new_employee
)

urlpatterns = [
    url(r'^$', employee, name='employee'),
    url(r'^new$', new_employee, name='new-employee'),
]
