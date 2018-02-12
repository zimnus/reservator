from django.conf.urls import url

from .views import (
    dashboard,
    detail,
    update
)

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),
    # OLD
    # url(r'^enterprise/create/$', create, name='create'),
    url(r'^enterprise/detail/(?P<pk>[\w-]+)/$', detail, name="detail"),
    url(r'^enterprise/update/(?P<pk>[\w-]+)/$', update, name="update"),
]