from django.conf.urls import url

from .views import StaffScheduleListView, StaffScheduleDetailView, StaffEventListView

urlpatterns = [
    url(r'^(?P<company_id>[\w-]+)/(?P<select_date>[\w-]+)/$', StaffScheduleListView.as_view(), name='schedule-list'),
    url(r'^event/(?P<company_id>[\w-]+)/(?P<staff_id>[\w-]+)/$', StaffEventListView.as_view(), name='event-list'),
    url(r'^(?P<company_id>[\w-]+)/(?P<staff_id>[\w-]+)/(?P<select_date>[\w-]+)/$',
        StaffScheduleDetailView.as_view(), name='schedule-detail'),
]
