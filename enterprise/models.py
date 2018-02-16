from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.conf import settings
from django.dispatch import receiver
import datetime

from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from geoposition.fields import GeopositionField

from jsonfield import JSONField

User = settings.AUTH_USER_MODEL


########## CHOICE ############

def upload_enterprise_image(instance, filename):
    return "enterprise/{title}/{filename}".format(title=instance.title, filename=filename)


########### QuerySet ##################
class EnterpriseQuerySet(models.QuerySet):
    # def search(self, query):
    #     if query:
    #         return self.filter(
    #             Q(name__icontains=query) |
    #             Q(employee__sex__iexact=query) |
    #             Q(employee__sex__icontains=query)
    #         ).distinct()
    #     return self
    pass


########### MANAGERS ##################
class EnterpriseManager(models.Manager):
    def get_queryset(self):
        return EnterpriseQuerySet(self.model, using=self._db)

    def get_employee(self, enterprise):
        from employee.models import Employee
        return Employee.objects.filter(enterprise=enterprise).filter(fired=False)

        # def search(self, query):
        #     return self.get_queryset().search(query)


########### Models ###############
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ('-name',)


class Enterprise(models.Model):
    owner = models.OneToOneField(User, help_text='Owner field')
    title = models.CharField(max_length=255, help_text='Name enterprise')
    logo = models.ImageField(upload_to=upload_enterprise_image, help_text='Logo image', blank=True)
    category = models.CharField(max_length=200, blank=True, null=True, help_text='Category')
    description = models.TextField(help_text='Short descriptions', blank=True)
    schedule = JSONField(blank=True, null=True, help_text='Schedule enterprise')
    city = models.ForeignKey(City, help_text='Select city', blank=True, null=True)
    address = models.CharField(max_length=255, help_text='Address enterprise', blank=True)
    phone = PhoneNumberField(max_length=255, help_text='Contact phone', blank=True)
    group_priority = models.PositiveIntegerField(help_text='Enterprise priority from filter', default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EnterpriseManager()

    class Meta:
        db_table = 'Enterprise'
        verbose_name = 'Enterprise'
        verbose_name_plural = 'Enterprises'
        ordering = ['-group_priority']

    def __str__(self):
        return str(self.title)[:50]

    def get_absolute_url(self):
        return reverse("enterprise:detail", kwargs={'pk': self.pk})

    def get_services(self):
        from service.models import Service
        return Service.objects.filter(enterprise__owner=self.pk)

    def get_employee(self):
        id = self.id
        return Enterprise.objects.get_employee(id)


# @receiver(post_save, sender=User)
# def create_enterprise(sender, instance, created, **kwargs):
#     if created:
#         Enterprise.objects.get_or_create(owner=instance)
