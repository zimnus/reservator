from django.conf.urls import url, include
from django.contrib import admin


from .views import UserDetailAPIView
urlpatterns = [
    url(r'^(?P<id>\d+)/$', UserDetailAPIView.as_view(), name='detail'),
]