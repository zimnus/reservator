from django.conf.urls import url

from .views import (
    base,
    base_edit,
    personal,
    service
)

urlpatterns = [
    url(r'^enterprise/$', base, name='enterprise-settings'),
    url(r'^change/edit=(?P<pk>[\w-]+)/$', base_edit, name='enterprise-settings-edit'),
    url(r'^group/company=(?P<pk>[\w-]+)/$', service, name='service-group'),
]
