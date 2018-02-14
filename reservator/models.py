import time

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


def _profile_upload_to(object, filename):
    extension = filename.split('.')[-1]
    return 'profile/{}.{}'.format(int(time.time() * 1000), extension)


class User(AbstractUser):
    image = models.ImageField('Photo', blank=True, upload_to=_profile_upload_to, max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    manager = models.BooleanField(default=False)
    client = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
        unique_together = ('email', )

    def __str__(self):
        return self.get_full_name()
