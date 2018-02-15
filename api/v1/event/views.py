from rest_framework import generics, mixins, permissions

from .serializer import EventSerializer
from event.models import Event


class EventView(generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
