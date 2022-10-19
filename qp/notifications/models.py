from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

CHOIX_TYPES = [
    ("success", _("Success")),
    ("error", _("Error"))
]

class qpNotification(models.Model):
    user_to = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name=_("To User"),
        blank=False,
        null=False
    )
    user_from = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="notifications_from",
        verbose_name=_("From User"),
        blank=True,
        null=True
    )
    content = models.TextField(
        verbose_name=_("Content"),
        blank=True,
        null=True
    )
    has_type = models.CharField(
        verbose_name=_("Type"),
        max_length=32,
        choices=CHOIX_TYPES,
        blank=True,
        null=True
    )
    is_seen = models.BooleanField(
        verbose_name=_("Seen"),
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True
    )

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ["-created_at"]
    
    def __str__(self):
        return "%s" % (str(_("Notification")))