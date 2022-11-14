from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from qp.characters.models import qpCharacter
from qp.forums.models import qpForum, qpForumCategory, qpForumSection
from qp.quests.models import qpQuest, qpQuestRewardCurrency, qpQuestLog
from qp.rpg.models import qpRpg, qpRpgSkill, qpRpgCurrency

User = get_user_model()

class QuestTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        rpg = qpRpg.objects.create(name="Test RPG")
        forum = qpForum.objects.create(rpg=rpg)
        category = qpForumCategory.objects.create(forum=forum, title="Test Category")
        section = qpForumSection.objects.create(forum=forum, category=category, title="Test Section")
        skill = qpRpgSkill.objects.create(rpg=rpg, name="Test Skill", attribute="strength")
        currency = qpRpgCurrency.objects.create(rpg=rpg, name="Test Currency")
        character = qpCharacter.objects.create(user=user, rpg=rpg, first_name="Test Character")
        # ===--- quest
        quest = qpQuest.objects.create(rpg=rpg, section=section, title="Test Quest", level=1)
        quest.skills.add(skill)
        quest.save()
        # ===--- quest_reward_currency
        qpQuestRewardCurrency.objects.create(quest=quest, currency=currency)
        # ===--- quest_log
        qpQuestLog.objects.create(quest=quest, character=character, start=timezone.now(), end=timezone.now()+quest.duration)

    def test_quest(self):
        """Quest"""
        q = qpQuest.objects.first()
        self.assertTrue(isinstance(q, qpQuest))
        self.assertEqual(q.__str__(), str(q.title))

    def test_quest_reward_currency(self):
        """Quest Reward Currency"""
        q = qpQuestRewardCurrency.objects.first()
        self.assertTrue(isinstance(q, qpQuestRewardCurrency))
        self.assertEqual(q.__str__(), str(q.currency.name))

    def test_quest_log(self):
        """Quest Log"""
        q = qpQuestLog.objects.first()
        self.assertTrue(isinstance(q, qpQuestLog))
        self.assertEqual(q.__str__(), "%s - %s" % (
            str(q.quest.title), str(q.character.name)
        ))
