from django.conf.urls import url

from .views import (
    service,
    service_detail,
    service_update,
    category_detail
)

urlpatterns = [
    url(r'^$', service, name='service'),
    url(r'^detail/(?P<service_id>[\w-]+)$', service_detail, name='service-detail'),
    url(r'^update/(?P<service_id>[\w-]+)$', service_update, name='service-update'),
    url(r'^category/detail/(?P<category_id>[\w-]+)$', category_detail, name='category-detail'),
]
