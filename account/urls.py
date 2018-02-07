from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile

urlpatterns = [
    url(r'^profile', profile, name='profile'),
    # auth
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', register, name='register'),
]