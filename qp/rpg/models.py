from django.utils.translation import gettext_lazy as _
from django.db import models
from ordered_model.models import OrderedModel
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


CHOIX_RESISTANCES = [
    ("physical", _("Physical Resistance")),
    ("mental", _("Mental Resistance")),
    ("spiritual", _("Spiritual Resistance"))
]

CHOIX_ATTRIBUTES = [
    ("strength", _("Strength")),
    ("constitution", _("Constitution")),
    ("dexterity", _("Dexterity")),
    ("perception", _("Perception")),
    ("intelligence", _("Intelligence")),
    ("willpower", _("Willpower"))
]


class qpRpg(models.Model):
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
        related_name="created_rpg",
        verbose_name=_("Creator"),
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="owned_rpg",
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
        upload_to="rpgs/icons",
        blank=True,
        null=True
    )
    is_public = models.BooleanField(
        verbose_name=_("Public"),
        default=True,
        help_text=_("Designates whether this RPG should be visible for everyone. Unselect this to make it visible only for staff.")
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_("Designates whether this RPG should be treated as active. Unselect this instead of deleting RPG.")
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
        verbose_name = _("RPG")
        verbose_name_plural = _("RPGs")
        ordering = ["name"]
    
    def __str__(self):
        return "%s" % (str(self.name))
    
    @property
    def initial(self):
        return "".join([x[0] for x in self.name.split()[:2]]).upper()
    
    def get_settings(self):
        if hasattr(self, "settings"):
            return self.settings
        return qpSettingsRpg.objects.filter(rpg__isnull=True).first()


class qpRpgRace(models.Model):
    rpg = models.ForeignKey(
        qpRpg,
        on_delete=models.CASCADE,
        related_name="races",
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    name_male = models.CharField(
        verbose_name=_("Male Name"),
        max_length=32,
        blank=True,
        null=True
    )
    name_female = models.CharField(
        verbose_name=_("Female Name"),
        max_length=32,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Race")
        verbose_name_plural = _("Races")
        ordering = ["name"]
    
    def __str__(self):
        return "%s" % (str(self.name))


class qpRpgSkill(models.Model):
    rpg = models.ForeignKey(
        qpRpg,
        on_delete=models.CASCADE,
        related_name="skills",
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    attribute = models.CharField(
        verbose_name=_("Attribute"),
        max_length=32,
        choices=CHOIX_ATTRIBUTES,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        ordering = ["name"]
    
    def __str__(self):
        return "%s" % (str(self.name))


class qpRpgCurrency(OrderedModel):
    rpg = models.ForeignKey(
        qpRpg,
        on_delete=models.CASCADE,
        related_name="currencies",
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    icon = models.CharField(
        verbose_name=_("Icon"),
        max_length=120,
        default="mdi mdi-cash-multiple",
        blank=False,
        null=False
    )
    order_with_respect_to = "rpg"

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ["rpg", "order"]
    
    def __str__(self):
        return "%s" % (str(self.name))


class qpRpgStyle(models.Model):
    rpg = models.ForeignKey(
        qpRpg,
        on_delete=models.CASCADE,
        related_name="style",
        verbose_name=_("RPG"),
        blank=False,
        null=False
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=32,
        blank=False,
        null=False
    )
    stylesheet = models.TextField(
        verbose_name=_("Stylesheet"),
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=False
    )

    class Meta:
        verbose_name = _("Style")
        verbose_name_plural = _("Styles")
        ordering = ["rpg", "name"]
    
    def __str__(self):
        return "%s" % (str(self.name))


class qpSettingsRpg(models.Model):
    rpg = models.OneToOneField(
        qpRpg,
        on_delete=models.CASCADE,
        related_name="settings",
        unique=True,
        blank=True,
        null=True
    )
    limit_characters = models.PositiveSmallIntegerField(
        verbose_name=_("Characters Limit"),
        default=100
    )
    limit_races = models.PositiveSmallIntegerField(
        verbose_name=_("Races Limit"),
        default=20
    )
    limit_skills = models.PositiveSmallIntegerField(
        verbose_name=_("Skills Limit"),
        default=60
    )
    limit_inventory_size_character = models.PositiveSmallIntegerField(
        verbose_name=_("Character Inventory Size Limit"),
        default=100
    )
    modifier_resistance_physical = models.SmallIntegerField(
        verbose_name=_("Physical Resistance Modifier"),
        default=0
    )
    modifier_resistance_mental = models.SmallIntegerField(
        verbose_name=_("Mental Resistance Modifier"),
        default=0
    )
    modifier_resistance_spiritual = models.SmallIntegerField(
        verbose_name=_("Spiritual Resistance Modifier"),
        default=0
    )
    total_attribute = models.PositiveSmallIntegerField(
        verbose_name=_("Total Attribute"),
        default=6
    )
    quest_malus_level_difference = models.FloatField(
        verbose_name=_("Malus of Quest Level Difference"),
        default=0.25
    )
    quest_modifier_destiny = models.FloatField(
        verbose_name=_("Modifier of Quest Destiny"),
        default=0.05
    )

    class Meta:
        verbose_name = _("RPG Setting")
        verbose_name_plural = _("RPG Settings")
        ordering = ["pk"]
    
    def __str__(self):
        if self.rpg:
            return "%s" % (str(_("Settings of %s") % (str(self.rpg.name))))
        return "%s" % (str(_("Settings")))