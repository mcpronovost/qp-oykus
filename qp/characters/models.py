from django.utils.translation import gettext_lazy as _
from django.db import models
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model

from qp.characters.utils import get_slugific_names


class qpCharacter(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="characters",
        verbose_name=_("User"),
        blank=False,
        null=False
    )
    first_name = models.CharField(
        verbose_name=_("First Name"),
        max_length=32,
        blank=False,
        null=False
    )
    middle_name = models.CharField(
        verbose_name=_("Middle Name"),
        max_length=32,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        verbose_name=_("Last Name"),
        max_length=32,
        blank=True,
        null=True
    )
    resistance_physical = models.PositiveSmallIntegerField(
        verbose_name=_("Physique Resistance"),
        default=0,
        blank=False,
        null=False
    )
    resistance_mental = models.PositiveSmallIntegerField(
        verbose_name=_("Mental Resistance"),
        default=0,
        blank=False,
        null=False
    )
    resistance_spiritual = models.PositiveSmallIntegerField(
        verbose_name=_("Spiritual Resistance"),
        default=0,
        blank=False,
        null=False
    )
    attribute_strength = models.PositiveSmallIntegerField(
        verbose_name=_("Strength"),
        default=0,
        blank=False,
        null=False
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
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")
        ordering = ["last_name", "middle_name", "first_name"]
    
    def __str__(self):
        return "%s" % (str(self.name))
    
    def name(self):
        result = "%s" % (str(self.first_name))
        if self.middle_name:
            result += " %s" % (str(self.middle_name))
        if self.last_name:
            result += " %s" % (str(self.last_name))
        return result