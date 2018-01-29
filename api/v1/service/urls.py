from django.conf.urls import url

from .views import (
    ServiceListView,
    ServiceCreateView
)

urlpatterns = [
    url(r'^$', ServiceListView.as_view(), name='service-list'),
    url(r'^create/(?P<company_id>[\w-]+)/(?P<service_id>[\w-]+)/$', ServiceCreateView.as_view(), name='service-create')
]
