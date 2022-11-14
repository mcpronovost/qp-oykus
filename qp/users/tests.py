from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.translation import gettext_lazy as _
from qp.users.models import qpUserProfile

User = get_user_model()

class UserTestCase(TestCase):
    def do_create(self, username="qamuy", name="Qamuy"):
        user = User.objects.create(username=username)
        return qpUserProfile.objects.create(user=user, name=name)

    def test_users_profile(self):
        """Users Profile"""
        p = self.do_create()
        self.assertTrue(isinstance(p, qpUserProfile))
        self.assertEqual(p.__str__(), str(_("Profile")))
        self.assertEqual(p.initial, "".join([x[0] for x in p.name.split()[:2]]).upper())
