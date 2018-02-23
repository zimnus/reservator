import random

from django.conf import settings
from django.contrib.auth import get_user_model


def generate_username():
    uid = u'U%010d' % random.randint(0, 10 ** 10)
    if get_user_model().objects.filter(username=uid).exists():
        return generate_username()
    return uid
