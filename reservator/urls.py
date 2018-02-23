from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # apps urls
    url(r'', include('enterprise.urls', namespace='enterprise')),
    url(r'^profile/', include('profile.urls', namespace='profile')),
    url(r'^employee/', include('employee.urls', namespace='employee')),
    url(r'^service/', include('service.urls', namespace='service')),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
    url(r'^settings/', include('settings.urls', namespace='settings')),
    # auth
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # Social
    url(r'^accounts/', include('allauth.urls')),
    # api
    url(r'^api/', include('api.urls', namespace='api')),
    # url(r'^api/enterprise/', include('enterprise.api.urls', namespace='api-enterprise')),
    # url(r'^api/employee/', include('employee.api.urls', namespace='api-employee')),
    # url(r'^api/profile/', include('account.api.profile.urls', namespace='api-profile')),
    # url(r'^api/auth/', include('account.api.urls', namespace='api-auth')),
    # admin
    url(r'^area51/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
