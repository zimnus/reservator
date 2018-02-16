from django import template

from enterprise.models import Enterprise
from employee.models import Employee

register = template.Library()


# @register.simple_tag
def user_ent(user):
    ent = Enterprise.objects.get(owner=user)
    return ent


def ent_id(user):
    r_id = Enterprise.objects.get(owner=user)
    return r_id.pk


def staff_list(ent):
    staff = Employee.objects.filter(enterprise=ent)
    return staff


register.filter('user_ent', user_ent)
register.filter('ent_id', ent_id)
register.filter('staff_list', staff_list)
