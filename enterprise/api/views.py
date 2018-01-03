import json
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView

from .serializer import EnterpriseSerializer
from enterprise.models import Enterprise


class EnterpriseAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    passed_id = None
    search_fields = ('title', 'short_descr', )
    serializer_class = EnterpriseSerializer

    def get_queryset(self):
        if not self.request.user.is_anonymous():
            return Enterprise.objects.filter(owner=self.request.user)
        return None

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
