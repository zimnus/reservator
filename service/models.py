from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import gettext_lazy as _

from enterprise.models import Enterprise


# Create your models here.
price = (
    ('UAH', 'UAH'),
    ('RUB', 'RUB')
)


class Category(models.Model):
    enterprise = models.ForeignKey(Enterprise, help_text='Select enterprise', related_name='services')
    title = models.CharField(max_length=255, help_text='Name category of services')
    weight = models.PositiveIntegerField(default=1, help_text='Priority')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'db_category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service:category-detail", kwargs={'category_id': self.pk})


class Service(models.Model):
    enterprise = models.ForeignKey(Enterprise, related_name='Owner')
    title = models.CharField(max_length=255, help_text='Name of service')
    service_desc = models.TextField(help_text='Short description', blank=True, null=True)
    service_duration = models.DurationField(blank=True, null=True, verbose_name=_('Service duration'))
    price = models.CharField(max_length=50, choices=price, help_text='Select currency', default='UAH')
    min_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_('Min price'))
    max_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_('Max price'))
    service = models.ForeignKey(Category, help_text='Select category', related_name='service')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access = models.BooleanField(default=False)

    class Meta:
        db_table = 'db_service'
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service:service-detail', kwargs={'service_id': self.pk})

    def get_update_url(self):
        return reverse('service:service-update', kwargs={'service_id': self.pk})
