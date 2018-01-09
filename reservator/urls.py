from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('enterprise.urls', namespace='enterprise')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^booking/', include('booking.urls', namespace='booking')),
    url(r'^api/enterprise/', include('enterprise.api.urls', namespace='api-enterprise')),
    url(r'^api/employee/', include('employee.api.urls', namespace='api-employee')),
    url(r'^api/user/', include('account.api.user.urls', namespace='api-user')),
    url(r'^api/auth/', include('account.api.urls', namespace='api-auth')),
    url(r'^area51/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
