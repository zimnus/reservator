import json
from rest_framework import generics, mixins, permissions

from .serializer import EnterpriseSerializer, CategoryOfServicesSerializers, CitySerializer
from enterprise.models import Enterprise, City
from service.models import Service


class EnterpriseAPIListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    # passed_id = 'id'
    search_fields = ('title', 'short_descr',)
    serializer_class = EnterpriseSerializer
    queryset = Enterprise.objects.all()


class EnterpriseAPIUserView(mixins.UpdateModelMixin, mixins.CreateModelMixin, generics.ListAPIView):
    permissions_class = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EnterpriseSerializer

    def get_queryset(self):
        return Enterprise.objects.filter(owner=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnterpriseAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EnterpriseSerializer
    lookup_field = 'id'
    queryset = Enterprise.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryOfServicesAPIListView(mixins.UpdateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategoryOfServicesSerializers

    # lookup_field = 'id'

    def get_queryset(self):
        return Service.objects.filter(enterprise=self.kwargs['id'])

    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(enterprise=self.kwargs['enterprise'])


class CategoryOfServiceAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategoryOfServicesSerializers
    lookup_field = 'id'
    queryset = Service.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
