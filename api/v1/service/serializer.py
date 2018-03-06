from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from service.models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'title',
            'service_desc',
            'service_duration',
            'price',
            'min_price',
            'max_price',
            'access',
            'service',
        )


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = (
            'url',
            'id',
            'title',
            'weight',
            'enterprise',
        )

    def get_url(self, obj):
        request = self.context.get('request')
        return api_reverse('api:api-service:category-detail', kwargs={'pk': obj.id}, request=request)


class CategoryDetailSerialize(serializers.ModelSerializer):
    # service = serializers.StringRelatedField(many=True, read_only=True)
    service = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'weight',
            'enterprise',
            'service'
        )
