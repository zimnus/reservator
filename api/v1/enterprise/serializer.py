from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from django.contrib.staticfiles.templatetags.staticfiles import static

from enterprise.models import Enterprise, City
from service.models import Service
from account.api.serializers import UserPublicSerializer


class EnterpriseSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)
    services = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Enterprise
        fields = (
            'uri',
            'id',
            'user',
            'title',
            'description',
            'logo',
            'city',
            'schedule',
            'address',
            'phone',
            'comment_count',
            'group_priority',
            'services',
        )
        read_only_fields = ('user',)

    def get_comment_count(self, obj):
        return 0

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api:api-enterprise:detail', kwargs={'id': obj.id}, request=request)

    def validate(self, data):
        logo = data.get('logo', None)
        if logo is None:
            serializers.ValidationError('Image is required!')
        return data


class CategoryOfServicesSerializers(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    employee = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Service
        fields = (
            'uri',
            'id',
            'title',
            'employee',
            'weight'
        )

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api:api-enterprise:service-detail', kwargs={'id': obj.id}, request=request)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
