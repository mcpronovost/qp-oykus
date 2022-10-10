from django.utils.translation import gettext_lazy as _
from django.db import models
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model

class qpProject(models.Model):
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
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="created_projects",
        verbose_name=_("Creator"),
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="owned_projects",
        verbose_name=_("Owner"),
        blank=True,
        null=True
    )
    caption = models.CharField(
        verbose_name=_("Caption"),
        max_length=120,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )
    primary_color = ColorField(
        verbose_name=_("Primary Colour"),
        default="#89a411",
        blank=False,
        null=False
    )
    icon = models.ImageField(
        verbose_name=_("Icon"),
        upload_to="projects/icons",
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        verbose_name=_("Public"),
        default=True,
        help_text=_("Designates whether this project should be visible for everyone. Unselect this to make it visible only for staff.")
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_("Designates whether this project should be treated as active. Unselect this instead of deleting project.")
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ["-updated_at"]
    
    def __str__(self):
        return "%s" % (str(self.name))
    
    @property
    def initial(self):
        return "".join([x[0] for x in self.name.split()[:2]]).upper()
