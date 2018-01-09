from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime

from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from geoposition.fields import GeopositionField

from account.models import ClientProfile

User = settings.AUTH_USER_MODEL

########## CHOICE ############

WORK_DAYS = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)


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
    def get_list(self, request_user):
        return Enterprise.objects.filter(owner=request_user)

    def employee_list(self, pk):
        from account.models import Employee
        return Employee.objects.filter(enterprise=pk)

    def get_queryset(self):
        return EnterpriseQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


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
    owner = models.ForeignKey(User, help_text='Owner field')
    title = models.CharField(max_length=255, help_text='Name enterprise')
    logo = models.ImageField(upload_to=upload_enterprise_image, help_text='Logo image')
    short_descr = models.TextField(help_text='Short descriptions')
    city = models.ForeignKey(City, help_text='Select city')
    schedule = models.TextField(help_text='Schedule enterprise')
    address = models.CharField(max_length=255, help_text='Address enterprise')
    phone = PhoneNumberField(max_length=255, help_text='Contact phone')
    coordinate_lat = models.FloatField(help_text='Latitude')
    coordinate_lon = models.FloatField(help_text='Longitude')
    active_stuff_count = models.PositiveIntegerField(default=0, help_text='Active stuff')
    group_priority = models.PositiveIntegerField(help_text='Enterprise priority from filter')

    objects = EnterpriseManager()

    class Meta:
        db_table = 'Enterprise'
        verbose_name = 'Enterprise'
        ordering = ['-group_priority']

    def __str__(self):
        return str(self.title)[:50]

    def get_absolute_url(self):
        return reverse("enterprise:detail", kwargs={'pk': self.pk})

    """
    def is_open_now(self):
        now = datetime.datetime.time(datetime.datetime.now())
        day = datetime.datetime.now().strftime("%A")
        active_days = list(self.days)
        # print("Time now - {}\n Work days: {}".format(now, day))
        if day.capitalize() in active_days:
            if self.open < self.close and self.open < now < self.close:
                return True
        return False
    """


class CategoryOfServices(models.Model):
    title = models.CharField(max_length=255, help_text='Name category of cervices')
    weight = models.PositiveIntegerField(default=1, help_text='Priority')
    enterprise = models.ForeignKey(Enterprise, help_text='Select enterprise', related_name='services')

    class Meta:
        db_table = 'Category_of_services'
        verbose_name = 'Category of service'
        verbose_name_plural = 'Category of services'

    def __str__(self):
        return self.title
