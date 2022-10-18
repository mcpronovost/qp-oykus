from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from django.db import models
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


class qpForum(models.Model):
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
    project = models.OneToOneField(
        "projects.qpProject",
        on_delete=models.SET_NULL,
        related_name="forum",
        verbose_name=_("Project"),
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="forums",
        verbose_name=_("Owner"),
        blank=True,
        null=True
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
        verbose_name = _("Forum")
        verbose_name_plural = _("Forums")
        ordering = ["name"]
    
    def __str__(self):
        return "%s" % (str(self.name))


class qpForumCategory(models.Model):
    forum = models.ForeignKey(
        qpForum,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name=_("Forum"),
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
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
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["title"]
    
    def __str__(self):
        return "%s" % (str(self.title))


class qpForumSection(models.Model):
    forum = models.ForeignKey(
        qpForum,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name=_("Forum"),
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        qpForumCategory,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name=_("Category"),
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
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
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")
        ordering = ["title"]
    
    def __str__(self):
        return "%s" % (str(self.title))


class qpForumTopic(models.Model):
    forum = models.ForeignKey(
        qpForum,
        on_delete=models.CASCADE,
        related_name="topics",
        verbose_name=_("Forum"),
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        qpForumCategory,
        on_delete=models.CASCADE,
        related_name="topics",
        verbose_name=_("Category"),
        blank=False,
        null=False
    )
    section = models.ForeignKey(
        qpForumSection,
        on_delete=models.CASCADE,
        related_name="topics",
        verbose_name=_("Section"),
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
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
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
        ordering = ["title"]
    
    def __str__(self):
        return "%s" % (str(self.title))


class qpForumMessage(models.Model):
    forum = models.ForeignKey(
        qpForum,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name=_("Forum"),
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        qpForumCategory,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name=_("Category"),
        blank=False,
        null=False
    )
    section = models.ForeignKey(
        qpForumSection,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name=_("Section"),
        blank=False,
        null=False
    )
    topic = models.ForeignKey(
        qpForumTopic,
        on_delete=models.CASCADE,
        related_name="messages",
        verbose_name=_("Topic"),
        blank=False,
        null=False
    )
    content = models.TextField(
        verbose_name=_("Content"),
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
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")
        ordering = ["pk"]
    
    def __str__(self):
        return "%s #%s" % (str(_("Message")), str(self.title))
