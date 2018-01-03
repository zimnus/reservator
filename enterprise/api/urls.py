from django.conf.urls import url

from .views import (
    EnterpriseAPIView,
    EnterpriseAPIDetailView
)

urlpatterns = [
    url(r'^$', EnterpriseAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', EnterpriseAPIDetailView.as_view(), name='detail'),
]
