from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from service.models import Service, Category


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'url',
            'title',
            'weight',
            'enterprise',
        )

    def get_url(self, obj):
        request = self.context.get('request')
        return api_reverse('api:api-service:category-detail', kwargs={'pk': obj.id}, request=request)


class CategoryDetailSerialize(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'title',
            'weight',
            'enterprise',
            'service'
        )


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
        )
