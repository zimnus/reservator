from rest_framework import generics, permissions, mixins
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .serializer import CategorySerializer, CategoryDetailSerialize, ServiceSerializer
from service.models import Category, Service


class CategoryListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Category.objects.filter(enterprise=company_id)


class CategoryDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategoryDetailSerialize
    queryset = Category


class ServiceListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ServiceSerializer

    def get_queryset(self):
        enterprise_id = self.kwargs['enterprise_id']
        return Service.objects.filter(enterprise=enterprise_id)


class ServiceFilterListView(generics.ListAPIView):
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
