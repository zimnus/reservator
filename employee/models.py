from django.db import models
from django.utils.translation import ugettext_lazy as _
from enterprise.models import Enterprise, CategoryOfServices


# Write you code here
def upload_employee_avatar_image(instance, filename):
    return "employees/{enterprise}/{filename}".format(enterprise=instance.enterprise.title, filename=filename)


class Employee(models.Model):
    enterprise = models.ForeignKey(Enterprise)
    name = models.CharField(max_length=255, help_text='Name of employees')
    specialization = models.CharField(max_length=255, help_text='Specialization')
    weight = models.PositiveIntegerField(default=1, help_text='Weight for sorted')
    show_rating = models.BooleanField(default=False, help_text='Show rating employees')
    rating = models.PositiveIntegerField(default=0, help_text='Rating')
    votes_count = models.PositiveIntegerField(default=0, help_text='Votes count')
    avatar = models.ImageField(upload_to=upload_employee_avatar_image, help_text='Avatar', blank=True)
    information = models.TextField(help_text='More info')
    hidden = models.BooleanField(default=False, help_text='Hidden for booking')
    fired = models.BooleanField(default=False, help_text='Is fired')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    service = models.ForeignKey(CategoryOfServices, help_text='Select category of services', related_name='employee')

    def __str__(self):
        return "{} {}".format(self.enterprise.title, self.specialization)

    class Meta:
        db_table = 'Employee'
        ordering = ['-weight']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
