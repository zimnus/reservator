import json
import datetime
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from schedule.models import StaffSchedule
from event.models import Event
from api.v1.event.serializer import EventSerializer


class StaffScheduleSerializer(serializers.ModelSerializer):
    staff = serializers.SerializerMethodField(read_only=True)
    staff_id = serializers.SerializerMethodField(read_only=True)
    event = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = StaffSchedule
        fields = (
            'staff',
            'staff_id',
            'work_date',
            'is_work',
            'schedule',
            'event'
        )

    @classmethod
    def get_staff_id(self, obj):
        return obj.staff.pk

    def get_staff(self, obj):
        return obj.staff.name

    def get_event(self, obj):
        qs = Event.objects.filter(staff=obj.staff).filter(start_event__icontains=str(obj.work_date))
        data = {
            'task': EventSerializer(qs, many=True).data
        }
        return data
