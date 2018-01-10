from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import ClientProfile


# Create your tests here.

class ClientProfileTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Test1', email='example@gmail.com')

    def test_foreign(self):
        user = User.objects.get(id=1)
        profile = ClientProfile.objects.get(id=user.id)
        field_label = profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, _('User'))

    def test_date_of_birth(self):
        pass
