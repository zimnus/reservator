from django.conf.urls import url

from .views import StaffScheduleListView

urlpatterns = [
    url(r'^(?P<company_id>[\w-]+)/$', StaffScheduleListView.as_view(), name='schedule-list')
]