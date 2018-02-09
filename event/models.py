from django.db import models

from enterprise.models import Enterprise
from employee.models import Employee
from service.models import Service

import datetime


# Create your models here.
class Event(models.Model):
    enterprise = models.ForeignKey(Enterprise)
    service = models.ForeignKey(Service)
    staff = models.ForeignKey(Employee)
    client = models.CharField(max_length=255)
    start_event = models.DateTimeField()
    end_event = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False, help_text='Task complete')

    def __str__(self):
        return self.service.title

    # record end time service
    def clean(self):
        duration = Service.objects.get(service=self.service.pk)
        self.end_event = self.start_event + duration.service_duration
