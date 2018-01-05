from rest_framework import serializers
from employee.models import Employee
from rest_framework.reverse import reverse as api_reverse


class EmployeeSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('api-employee:detail', kwargs={'id': obj.id}, request=request)
