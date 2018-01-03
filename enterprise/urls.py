from django.conf.urls import url

from .views import enterprise_list, enterprise_detail, create_enterprise, register_employee

urlpatterns = [
    url(r'^$', enterprise_list, name='list'),
    url(r'^enterprise/create/$', create_enterprise, name='create'),
    url(r'^enterprise/new_employee/(?P<pk>[\w-]+)/$', register_employee, name='employees'),
    url(r'^enterprise/detail/(?P<pk>[\w-]+)/$', enterprise_detail, name="detail"),
]