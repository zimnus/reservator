from django.db import models
from jsonfield import JSONField
from employee.models import Employee


# Create your models here.

class StaffSchedule(models.Model):
    staff = models.ForeignKey(Employee, related_name='Employee')
    work_date = models.DateField(help_text='Date work')
    is_work = models.BooleanField(default=True, help_text='Is employee work!')
    schedule = JSONField(blank=True, null=True, help_text='Schedule employee')

    def __str__(self):
        return "Staff: {}, date: {}".format(self.staff.name, self.work_date)

    class Meta:
        verbose_name = 'Staff schedule'
        verbose_name_plural = 'Staff schedules'
        db_table = 'Staff schedule'
