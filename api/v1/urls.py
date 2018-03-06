from django.conf.urls import url, include

urlpatterns = [
    url(r'^enterprises/', include('api.v1.enterprise.urls', namespace='api-enterprise')),
    url(r'^schedules/', include('api.v1.schedule.urls', namespace='api-schedule')),
    url(r'^services/', include('api.v1.service.urls', namespace='api-service')),
    url(r'^events/', include('api.v1.event.urls', namespace='api-event')),
    url(r'^accounts/', include('api.v1.accounts.urls', namespace='api-profile')),
    url(r'^user/', include('api.v1.accounts.user.urls', namespace='api-user')),
]