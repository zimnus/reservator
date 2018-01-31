from django.conf.urls import url

from .views import (
    service,
    service_detail,
    service_update,
    create_category,
    create_service,
    category_detail
)

urlpatterns = [
    url(r'^$', service, name='service'),
    url(r'^create/category', create_category, name='create-category'),
    url(r'^create/service$', create_service, name='create-service'),
    url(r'^detail/(?P<service_id>[\w-]+)$', service_detail, name='service-detail'),
    url(r'^update/(?P<service_id>[\w-]+)$', service_update, name='service-update'),
    url(r'^category/detail/(?P<category_id>[\w-]+)$', category_detail, name='category-detail'),
]
