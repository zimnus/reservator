from django.conf.urls import url

from .views import StaffScheduleListView

urlpatterns = [
    url(r'^(?P<company_id>[\w-]+)/(?P<select_date>[\w-]+)/$', StaffScheduleListView.as_view(), name='schedule-list')
]