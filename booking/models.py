from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from employee.models import Employee
from enterprise.models import Enterprise


# Create your models here.

######## Manager ##################

class BookingManager(models.Manager):
    def active(self, enterprise):
        return OnlineBooking.objects.all().filter(status=False, enterprise=enterprise)

    def complete(self, enterprise):
        return OnlineBooking.objects.all().filter(status=True, enterprise=enterprise)


######## Models ###################

class OnlineBooking(models.Model):
    executor = models.ForeignKey(Employee)
    enterprise = models.ForeignKey(Enterprise)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    client_name = models.CharField(max_length=255, help_text='First and Last name')
    client_phone = PhoneNumberField(help_text='Contact phone in format (+*********)')
    description = models.TextField()

    objects = BookingManager()

    def __str__(self):
        return "{} {}".format(self.executor.first_name, self.executor.last_name)

    class Meta:
        verbose_name = 'Online Booking'
        verbose_name_plural = 'Online Booking'
        db_table = 'online_booking'
        ordering = ['-date', ]
