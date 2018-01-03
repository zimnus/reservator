from rest_framework import generics, mixins, permissions

from employee.models import Employee
from .serializer import EmployeeSerializer


class EmployeeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    passed_id = None

    # def post(self, request, *args, **kwargs):
    #     return self.create(self, *args, **kwargs)
    #
    # def perform_create(self, serializer):
    #     serializer.save(enterprise=self.id)


class EmployeeAPIDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'
