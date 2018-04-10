from rest_framework import generics, mixins, permissions

from .serializer import StaffScheduleSerializer
from schedule.models import StaffSchedule


class StaffScheduleListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StaffScheduleSerializer

    # queryset = StaffSchedule.objects.all()
    def get_queryset(self):
        return StaffSchedule.objects.filter(staff__enterprise=self.kwargs['company_id'])\
            .filter(work_date=self.kwargs['select_date'])


class StaffScheduleDetailView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StaffScheduleSerializer

    def get_queryset(self):
        return StaffSchedule.objects.filter(staff__enterprise=self.kwargs['company_id'])\
            .filter(staff_id=self.kwargs['staff_id'])\
            .filter(work_date=self.kwargs['select_date'])


class StaffEventListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StaffScheduleSerializer

    def get_queryset(self):
        return StaffSchedule.objects.filter(staff__enterprise=self.kwargs['company_id'])\
            .filter(staff_id=self.kwargs['staff_id'])
