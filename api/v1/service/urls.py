from django.conf.urls import url

from .views import (
    ServiceListView,
    ServiceCreateView,
    CategoryListView
)

urlpatterns = [
    url(r'^(?P<category_id>[\w-]+)/$', ServiceListView.as_view(), name='service-list'),
    url(r'^create/(?P<company_id>[\w-]+)/(?P<service_id>[\w-]+)/$', ServiceCreateView.as_view(), name='service-create'),
    url(r'^category/(?P<company_id>[\w-]+)/$', CategoryListView.as_view(), name='category-list')
]
