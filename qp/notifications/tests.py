from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from qp.notifications.models import qpNotification

User = get_user_model()

class NotificationsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuserfornotifications")
        qpNotification.objects.create(user_to=user)

    def test_quest(self):
        """Notification"""
        q = qpNotification.objects.first()
        self.assertTrue(isinstance(q, qpNotification))
        self.assertEqual(q.__str__(), str(_("Notification")))
