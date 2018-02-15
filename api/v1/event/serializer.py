from rest_framework import serializers

from event.models import Event


class EventSerializer(serializers.ModelSerializer):
    staff = serializers.SerializerMethodField(read_only=True)
    staff_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Event
        exclude = ('created_at', 'updated_at')

    def get_staff(self, obj):
        return obj.staff.name

    def get_staff_id(self, obj):
        return obj.staff.pk