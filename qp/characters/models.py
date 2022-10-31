from django.utils.translation import gettext_lazy as _
from django.db import models
from autoslug import AutoSlugField
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model


class qpCharacter(models.Model):
    CHOIX_GENDERS = [
        ("unknown", _("Unknown")),
        ("male", _("Male")),
        ("female", _("Female"))
    ]
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="characters",
        verbose_name=_("User"),
        blank=False,
        null=False
    )
    rpg = models.ForeignKey(
        "rpg.qpRpg",
        on_delete=models.CASCADE,
        related_name="characters",
        verbose_name=_("RPG"),
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
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=32,
        choices=CHOIX_GENDERS,
        default="unknown",
        blank=False,
        null=False
    )
    race = models.ForeignKey(
        "rpg.qpRpgRace",
        on_delete=models.SET_NULL,
        related_name="characters",
        verbose_name=_("Race"),
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"),
        upload_to="characters/avatars",
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        "forums.qpForumSection",
        on_delete=models.SET_NULL,
        related_name="characters",
        verbose_name=_("Location"),
        blank=True,
        null=True
    )
    resistance_physical = models.PositiveSmallIntegerField(
        verbose_name=_("Physical Resistance"),
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
    attribute_constitution = models.PositiveSmallIntegerField(
        verbose_name=_("Constitution"),
        default=0,
        blank=False,
        null=False
    )
    attribute_dexterity = models.PositiveSmallIntegerField(
        verbose_name=_("Dexterity"),
        default=0,
        blank=False,
        null=False
    )
    attribute_perception = models.PositiveSmallIntegerField(
        verbose_name=_("Perception"),
        default=0,
        blank=False,
        null=False
    )
    attribute_intelligence = models.PositiveSmallIntegerField(
        verbose_name=_("Intelligence"),
        default=0,
        blank=False,
        null=False
    )
    attribute_willpower = models.PositiveSmallIntegerField(
        verbose_name=_("Willpower"),
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
    
    @property
    def name(self):
        result = "%s" % (str(self.first_name))
        if self.middle_name:
            result += " %s" % (str(self.middle_name))
        if self.last_name:
            result += " %s" % (str(self.last_name))
        return result
    
    @property
    def initial(self):
        return "".join([x[0] for x in self.name.split()[:3]]).upper()
    
    @property
    def physical(self):
        result = self.resistance_physical
        return result
    
    @property
    def mental(self):
        result = self.resistance_mental
        return result
    
    @property
    def spiritual(self):
        result = self.resistance_spiritual
        return result
    
    @property
    def strength(self):
        result = self.attribute_strength
        return result
    
    @property
    def constitution(self):
        result = self.attribute_constitution
        return result
    
    @property
    def dexterity(self):
        result = self.attribute_dexterity
        return result
    
    @property
    def perception(self):
        result = self.attribute_perception
        return result
    
    @property
    def intelligence(self):
        result = self.attribute_intelligence
        return result
    
    @property
    def willpower(self):
        result = self.attribute_willpower
        return result
    
    def get_wallet(self):
        result = {}
        for c in self.rpg.currencies.all():
            cc, _ = c.characters_currencies.get_or_create(
                character=self
            )
            result[cc.currency.name] = cc.amount
        return result


class qpCharacterSkill(models.Model):
    character = models.ForeignKey(
        qpCharacter,
        on_delete=models.CASCADE,
        related_name="skills",
        verbose_name=_("Character"),
        blank=False,
        null=False
    )
    skill = models.ForeignKey(
        "rpg.qpRpgSkill",
        on_delete=models.CASCADE,
        related_name="characters",
        verbose_name=_("Skill"),
        blank=False,
        null=False
    )
    exp = models.PositiveBigIntegerField(
        verbose_name=_("Experience"),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        ordering = ["skill"]
    
    def __str__(self):
        return "%s" % (str(self.skill.name))


class qpCharacterCurrency(models.Model):
    character = models.ForeignKey(
        qpCharacter,
        on_delete=models.CASCADE,
        related_name="currencies",
        verbose_name=_("Character"),
        blank=False,
        null=False
    )
    currency = models.ForeignKey(
        "rpg.qpRpgCurrency",
        on_delete=models.CASCADE,
        related_name="characters_currencies",
        verbose_name=_("Currency"),
        blank=False,
        null=False
    )
    amount = models.IntegerField(
        verbose_name=_("Amount"),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ["character", "currency"]
    
    def __str__(self):
        return "%s - %s" % (
            str(self.character.name),
            str(self.currency.name)
        )
