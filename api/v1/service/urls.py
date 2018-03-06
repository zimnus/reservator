from django.conf.urls import url

from .views import (
    ServiceListView,
    ServiceFilterListView,
    ServiceCreateView,
    CategoryListView,
    CategoryDetailView
)

urlpatterns = [
    url(r'^(?P<enterprise_id>[\w-]+)/$', ServiceListView.as_view(), name='service-list'),
    url(r'^filter/(?P<category_id>[\w-]+)/$', ServiceFilterListView.as_view(), name='service-filter'),
    url(r'^create/(?P<company_id>[\w-]+)/(?P<service_id>[\w-]+)/$', ServiceCreateView.as_view(), name='service-create'),
    url(r'^category/(?P<company_id>[\w-]+)/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category/detail/(?P<pk>[\w-]+)/$', CategoryDetailView.as_view(), name='category-detail'),
]
