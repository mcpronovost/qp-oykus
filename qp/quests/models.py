from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from ordered_model.models import OrderedModel

class qpQuest(OrderedModel):
    rpg = models.ForeignKey(
        "rpg.qpRpg",
        on_delete=models.CASCADE,
        related_name="quests",
        blank=False,
        null=False
    )
    section = models.ForeignKey(
        "forums.qpForumSection",
        on_delete=models.CASCADE,
        related_name="quests",
        blank=False,
        null=False
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
        blank=False,
        null=False
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=False,
        null=False
    )
    level = models.PositiveSmallIntegerField(
        verbose_name=_("Level"),
        default=1,
        blank=False,
        null=False
    )
    skills = models.ManyToManyField(
        "rpg.qpRpgSkill",
        related_name="quests",
        verbose_name=_("Skills"),
        blank=False
    )
    duration = models.DurationField(
        verbose_name=_("Duration"),
        default=timezone.timedelta(seconds=30)
    )
    reward_exp = models.PositiveIntegerField(
        verbose_name=_("Reward Experience"),
        default=1
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True
    )
    order_with_respect_to = "section"

    class Meta:
        verbose_name = _("Quest")
        verbose_name_plural = _("Quests")
        ordering = ["section", "order"]
    
    def __str__(self):
        return "%s" % (str(self.title))


class qpQuestRewardCurrency(models.Model):
    quest = models.ForeignKey(
        qpQuest,
        on_delete=models.CASCADE,
        related_name="reward_currencies",
        verbose_name=_("Quest"),
        blank=False,
        null=False
    )
    currency = models.ForeignKey(
        "rpg.qpRpgCurrency",
        on_delete=models.CASCADE,
        related_name="quest_reward_currencies",
        verbose_name=_("Currency"),
        blank=False,
        null=False
    )
    amount_min = models.IntegerField(
        verbose_name=_("Min Amount"),
        default=0,
        blank=False,
        null=False
    )
    amount_max = models.IntegerField(
        verbose_name=_("Max Amount"),
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")
        ordering = ["quest", "currency"]
    
    def __str__(self):
        return "%s" % (str(self.currency.name))


class qpQuestLog(models.Model):
    quest = models.ForeignKey(
        qpQuest,
        on_delete=models.CASCADE,
        related_name="logs",
        verbose_name=_("Quest"),
        blank=False,
        null=False
    )
    character = models.ForeignKey(
        "characters.qpCharacter",
        on_delete=models.CASCADE,
        related_name="questlogs",
        verbose_name=_("Character"),
        blank=False,
        null=False
    )
    start = models.DateTimeField(
        verbose_name=_("Start at"),
        blank=False,
        null=False
    )
    end = models.DateTimeField(
        verbose_name=_("End at"),
        blank=False,
        null=False
    )
    is_completed = models.BooleanField(
        verbose_name=_("Completed"),
        default=False
    )
    is_success = models.BooleanField(
        verbose_name=_("Success"),
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
        verbose_name = _("Quest Log")
        verbose_name_plural = _("Quest Logs")
        ordering = ["-start"]
    
    def __str__(self):
        return "%s - %s" % (
            str(self.quest.title),
            str(self.character.name)
        )
