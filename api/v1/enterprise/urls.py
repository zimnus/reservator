from django.conf.urls import url

from .views import (
    EnterpriseAPIListView,
    EnterpriseAPIUserView,
    EnterpriseAPIDetailView,
    CategoryOfServicesAPIListView,
    CategoryOfServiceAPIDetailView
)

urlpatterns = [
    url(r'^$', EnterpriseAPIListView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', EnterpriseAPIUserView.as_view(), name='list-user'),
    url(r'^detail/(?P<id>\d+)/$', EnterpriseAPIDetailView.as_view(), name='detail'),
    url(r'^(?P<id>\d+)/service/$', CategoryOfServicesAPIListView.as_view(), name='services'),
    url(r'^service/(?P<id>\d+)/detail/$', CategoryOfServiceAPIDetailView.as_view(), name='service-detail'),
]
