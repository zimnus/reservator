from django.db import models
from django.core.urlresolvers import reverse

from enterprise.models import Enterprise


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, help_text='Name category of cervices')
    weight = models.PositiveIntegerField(default=1, help_text='Priority')
    enterprise = models.ForeignKey(Enterprise, help_text='Select enterprise', related_name='services')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Category_of_services'
        verbose_name = 'Category of service'
        verbose_name_plural = 'Category of services'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service:category-detail", kwargs={'category_id': self.pk})


class Service(models.Model):
    enterprise = models.ForeignKey(Enterprise, related_name='Owner')
    title = models.CharField(max_length=255, help_text='Name of service')
    service_desc = models.TextField(help_text='Short description', blank=True, null=True)
    service_duration = models.DurationField(blank=True, null=True)
    min_price = models.PositiveIntegerField(default=0)
    max_price = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Category, help_text='Select category', related_name='service')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access = models.BooleanField(default=False)

    class Meta:
        db_table = 'Service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service:service-detail', kwargs={'service_id': self.pk})

    def get_update_url(self):
        return reverse('service:service-update', kwargs={'service_id': self.pk})
