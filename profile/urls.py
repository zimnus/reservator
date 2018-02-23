from django.conf.urls import url

from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, CreateClientView, CreateManagerView

urlpatterns = [
    url(r'^profile', profile, name='profile'),
    # auth
    url(r'^login/$', LoginView.as_view(), name='login'),
    # OLD
    # url(r'^register/$', register, name='register'),
    # Create Client (test)
    url(r'^client_register', CreateClientView.as_view(), name='create-client'),
    url(r'^manager_register', CreateManagerView.as_view(), name='create-manager'),
]