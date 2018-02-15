from django.db import models

from enterprise.models import Enterprise
from employee.models import Employee
from service.models import Service
from account.models import ClientProfile

import datetime


# Create your models here.
class Event(models.Model):
    enterprise = models.ForeignKey(Enterprise, help_text='Компания', related_name="Компания")
    service = models.ForeignKey(Service, help_text='Тип услуги', related_name="services")
    staff = models.ForeignKey(Employee, related_name='staff_event', help_text='Исполнитель')
    client = models.ForeignKey(ClientProfile, help_text='Профиль клиента', related_name="Слиент")
    start_event = models.DateTimeField(help_text='Дата и время начала сеанса')
    end_event = models.DateTimeField(blank=True, help_text='Дата и время окончания услуги')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(default=False, help_text='Статус заказа услуги')
    success = models.BooleanField(default=False, help_text='Услуга была наданна')
    complete = models.BooleanField(default=False, help_text='Услуга завершена')
    comment = models.TextField(blank=True, null=True, help_text="Дополнительные коментарии")

    def __str__(self):
        return self.service.title

    # record end-time service
    def clean(self):
        duration = Service.objects.get(pk=self.service.pk)
        self.end_event = self.start_event + duration.service_duration

    class Meta:
        db_table = 'event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
