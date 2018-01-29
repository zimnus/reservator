from django.conf.urls import url, include

urlpatterns = [
    # Stable
    url(r'', include('api.v1.urls')),
    # Version
    url(r'^v1/', include('api.v1.urls')),
]