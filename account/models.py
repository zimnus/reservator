from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

# from enterprise.models import Enterprise
# Create your models here.

User = settings.AUTH_USER_MODEL

SEX = (
    ('Men', 'Men'),
    ('Women', 'Women')
)


class ClientProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name=_('User'))
    sex = models.CharField(choices=SEX, max_length=50, help_text=_(u"Gender"), verbose_name=_(u'Gender'))
    birth = models.DateField(blank=True,
                             help_text=_('You date of birth'), null=True)
    address = models.CharField(max_length=255, help_text=_(u'Contact address: City, Str, apt'),
                               verbose_name=_(u'Address'))
    contact_email = models.EmailField(help_text='example@provider.com', blank=True)
    about = models.TextField(help_text=_('Say something about yourself'), blank=True)

    def __str__(self):
        return self.user.username

    @staticmethod
    def get(user: settings.AUTH_USER_MODEL):
        return ClientProfile.objects.get_or_create(user=user)[0]

    @staticmethod
    def create(user: settings.AUTH_USER_MODEL, password: str, **kwargs):
        client = ClientProfile.objects.create(user=user, **kwargs)
        client.save()
        return client

    def update_phone(self, phone):
        self.user.phone = phone
        self.user.save()

    def get_client_url(self):
        return reverse('account:client', kwargs={'pk': self.pk})

    class Meta:
        db_table = "client_profile"
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        unique_together = ('user', 'address', 'contact_email',)


# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         ClientProfile.get(instance)
#
#
# post_save.connect(post_save_user_receiver, sender=User)
