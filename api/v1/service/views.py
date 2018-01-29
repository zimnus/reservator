from rest_framework import generics, permissions, mixins

from .serializer import ServiceSerializer
from service.models import Service


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceCreateView(generics.CreateAPIView, mixins.CreateModelMixin):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, servise=self.request.get['service_id'])


class ServiceUpdateView(generics.UpdateAPIView):
    serializer_class = ServiceSerializer


class ServiceDeleteView(generics.DestroyAPIView):
    pass
