from rest_framework import generics, permissions, mixins

from .serializer import CategorySerializer, ServiceSerializer
from service.models import Category, Service


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Category.objects.filter(enterprise=company_id)


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Service.objects.filter(service=category_id)


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
