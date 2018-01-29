from django.conf.urls import url

from .views import (
    dashboard,
    enterprise,
    detail,
    create
)

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    url(r'^enterprise$', enterprise, name='enterprise'),
    url(r'^enterprise/create/$', create, name='create'),
    url(r'^enterprise/detail/(?P<pk>[\w-]+)/$', detail, name="detail"),
]