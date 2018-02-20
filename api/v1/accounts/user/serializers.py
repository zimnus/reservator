import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'uri'
        )

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api:api-user:detail', kwargs={"id": obj.id}, request=request)
