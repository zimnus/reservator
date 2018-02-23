from django.utils import timezone
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.template.loader import get_template
from django.core.mail import send_mail

import time

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


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
        unique_together = ('email',)

    def __str__(self):
        return self.get_full_name()


# class EmailActivationQuerySet(models.query.QuerySet):
#     def confirmable(self):
#         now = timezone.now()
#         start_range = now - timedelta(DEFAULT_ACTIVATION_DAYS)
#         end_range = now
#         return self.filter(
#             activated=False,
#             forced_expiret=False,
#         ).filter(
#             timestamp__gt=start_range,
#             timestamp__lte=end_range
#         )
#
#
# class EmailActivationManager(models.Manager):
#     def get_queryset(self):
#         return EmailActivationQuerySet(self.model, using=self._db)
#
#     def confirmable(self):
#         return self.get_queryset().confirmable()
#
#     def email_exists(self, email):
#         return self.get_queryset().filter(
#             Q(email=email) |
#             Q(user__email=email)
#         ).filter(
#             activated=False
#         )
#
#
# class EmailActivation(models.Model):
#     user = models.ForeignKey(User)
#     email = models.EmailField()
#     key = models.CharField(max_length=120)
#     activated = models.BooleanField(default=False)
#     forced_expired = models.BooleanField(default=False)
#     expired = models.IntegerField(default=7)
#     timestamp = models.DateTimeField(auto_now=True)
#
#     objects = EmailActivationManager()
#
#     def __str__(self):
#         return self.email
#
#     def can_activated(self):
#         qs = EmailActivation.objects.filter(pk=self.pk).confirmable()
#         if qs.exists():
#             return True
#         return False
#
#     def activate(self):
#         if self.can_activated():
#             user = self.user
#             user.is_active = True
#             user.save()
#             return True
#         return False
#
#     def regenerate(self):
#         self.key = None
#         self.save()
#         if self.key is not None:
#             return True
#         return False
#
#     def send_activation(self):
#         if not self.activated and not self.forced_expired:
#             if self.key:
#                 base_url = getattr(settings, 'BASE_URL', 'http://localhost:8000')
#                 key_path = reverse("account:email-activate", kwargs={'key': self.key})
#                 path = "{base}{path}".format(base=base_url, path=key_path)
#                 context = {
#                     'path': path,
#                     'email': self.email
#                 }
#                 txt_ = get_template("registration/emails/verify.txt").render(context)
#                 html_ = get_template("registration/emails/verify.html").render(context)
#                 subject = '1 Click email verification'
#                 from_email = settings.DEFAULT_FROM_EMAIL
#                 recipient_list = [self.email]
#                 sent_mail = send_mail(
#                     subject,
#                     txt_,
#                     from_email,
#                     recipient_list,
#                     html_message=html_,
#                     fail_silently=False
#                 )
#                 return sent_mail
#         return False
