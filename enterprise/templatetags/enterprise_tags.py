from django import template

from enterprise.models import Enterprise

register = template.Library()


# @register.simple_tag
def user_ent(user):
    ent = Enterprise.objects.get(owner=user)
    return ent


def ent_id(user):
    r_id = Enterprise.objects.get(owner=user)
    return r_id.pk


register.filter('user_ent', user_ent)
register.filter('ent_id', ent_id)
