from django.conf.urls import url

from .views import (
    service,
    create_category,
    create_service
)

urlpatterns = [
    url(r'^$', service, name='service'),
    url(r'^create$', create_service, name='create-service'),
]
