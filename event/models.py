from django.db import models

from enterprise.models import Enterprise
from employee.models import Employee
from service.models import Service


# Create your models here.
class Event(models.Model):
    enterprise = models.ForeignKey(Enterprise)
    service = models.ForeignKey(Service)
    staff = models.ForeignKey(Employee)
    client = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service.title
