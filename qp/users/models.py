from django.utils.translation import gettext_lazy as _
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

class qpUserProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("User"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    slug = AutoSlugField(
        verbose_name=_("Slug"),
        populate_from="name",
        unique=True,
        editable=True,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profile")