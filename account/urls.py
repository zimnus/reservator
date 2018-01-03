from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from .views import profile, register, edit

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit$', edit, name='edit'),
]