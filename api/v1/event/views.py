from rest_framework import generics, mixins, permissions

from .serializer import EventSerializer, EventDetailSerializer
from event.models import Event


class EventView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventDetailView(mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
