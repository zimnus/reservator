from django.conf.urls import url

from .views import StaffScheduleListView, StaffScheduleDetailView

urlpatterns = [
    url(r'^(?P<company_id>[\w-]+)/(?P<select_date>[\w-]+)/$', StaffScheduleListView.as_view(), name='schedule-list'),
    url(r'^(?P<company_id>[\w-]+)/(?P<staff_id>[\w-]+)/(?P<select_date>[\w-]+)/$',
        StaffScheduleDetailView.as_view(), name='schedule-detail'),
]
