from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from schedule.models import StaffSchedule


class StaffScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffSchedule
        fields = (
            'staff',
            'work_date',
            'is_work',
            'schedule'
        )
