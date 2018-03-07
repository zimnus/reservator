from django.conf.urls import url

from .views import (
    enterprise_update,
    update_logo,
    personal,
    add_employee,
    personal_detail,
    new_category,
    service,
    new_service
)

urlpatterns = [
    url(r'^change/update/(?P<pk>[\w-]+)/$', enterprise_update, name='enterprise-settings'),
    url(r'^change/logo/(?P<pk>[\w-]+)/$', update_logo, name='enterprise-logo'),
    url(r'^change/personal/(?P<pk>[\w-]+)/$', personal, name='personal-settings'),
    url(r'^service/create-serivce', new_service, name='new-service'),
    url(r'^personal/add', add_employee, name='add-personal'),
    url(r'^personal/update(?P<pk>[\w-]+)/$', personal_detail, name='staff-detail'),
    url(r'^group/company-(?P<pk>[\w-]+)/$', service, name='service-group'),
    url(r'^group/new/(?P<pk>[\w-]+)/$', new_category, name='new-category'),
]
