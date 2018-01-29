from django.conf.urls import url, include

urlpatterns = [
    url(r'^enterprises/', include('api.v1.enterprise.urls', namespace='api-enterprise')),
    url(r'^schedules/', include('api.v1.schedule.urls', namespace='api-schedule')),
    url(r'^services/', include('api.v1.service.urls', namespace='api-service')),
]