from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from enterprise.models import Enterprise, CategoryOfServices


class EnterpriseSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Enterprise
        fields = (
            'uri',
            'id',
            'title',
            'short_descr',
            'logo',
            'city',
            'schedule',
            'address',
            'phone',
            'comment_count',
            'coordinate_lat',
            'coordinate_lon',
            'active_stuff_count',
            'group_priority',
            'services',
        )

    def get_comment_count(self, obj):
        return 0

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-enterprise:detail', kwargs={'id': obj.id}, request=request)

    def validate(self, data):
        logo = data.get('logo', None)
        if logo is None:
            serializers.ValidationError('Image is required!')
        return data


class CategoryOfServicesSerializers(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    employee = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CategoryOfServices
        fields = (
            'uri',
            'id',
            'title',
            'employee',
            'weight'
        )

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-enterprise:service-detail', kwargs={'id': obj.id}, request=request)
