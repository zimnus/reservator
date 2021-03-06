from django.conf.urls import url

from .views import EventView


urlpatterns = [
    url(r'^$', EventView.as_view(), name='event-list'),
    url(r'^detail/(?P<id>\d+)/$', EventView.as_view(), name='event-detail'),
]