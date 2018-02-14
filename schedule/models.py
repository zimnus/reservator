from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from jsonfield import JSONField
from employee.models import Employee


# Create your models here.

class StaffSchedule(models.Model):
    staff = models.ForeignKey(Employee, related_name='Сотрудник', verbose_name="Сотрудник")
    work_date = models.DateField("День", help_text='День')
    is_work = models.BooleanField("Доступен", default=True, help_text='Доступен для записи')
    schedule = JSONField("График работы", blank=True, null=True, help_text='Распорядок дня')

    def __str__(self):
        return "Staff: {}, date: {}".format(self.staff.name, self.work_date)

    class Meta:
        verbose_name = _('График сотрудника')
        verbose_name_plural = _('График сотрудников')
        db_table = 'staff_schedule'
        unique_together = (('staff', 'work_date'), )
