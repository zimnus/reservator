from rest_framework import serializers

from service.models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'title',
            'service_duration',
            'min_price',
            'max_price',
            'service',
            'staff',
        )
