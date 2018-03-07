from rest_framework import generics

from .serializers import EmployeeSerializer

from employee.models import Employee


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        return Employee.objects.filter(enterprise__owner=self.request.user)