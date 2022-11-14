from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.translation import gettext_lazy as _
from qp.characters.models import qpCharacter, qpCharacterSkill
from qp.rpg.models import qpRpg, qpRpgSkill

User = get_user_model()

class CharacterTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuserforcharacter")
        rpg = qpRpg.objects.create(name="Test RPG")
        skill = qpRpgSkill.objects.create(rpg=rpg, name="Test Skill", attribute="strength")
        # ===--- character
        character = qpCharacter.objects.create(user=user, rpg=rpg, first_name="Test Character")
        # ===--- character_skill
        qpCharacterSkill.objects.create(character=character, skill=skill)

    def test_character(self):
        """Character"""
        q = qpCharacter.objects.first()
        self.assertTrue(isinstance(q, qpCharacter))
        self.assertEqual(q.__str__(), str(q.name))
        self.assertIsNotNone(q.name)
        self.assertTrue(isinstance(q.name, str))
        self.assertEqual(q.initial, "".join([x[0] for x in q.name.split()[:3]]).upper())
        self.assertGreaterEqual(q.physical, 0)
        self.assertGreaterEqual(q.mental, 0)
        self.assertGreaterEqual(q.spiritual, 0)
        self.assertGreaterEqual(q.strength, 0)
        self.assertGreaterEqual(q.constitution, 0)
        self.assertGreaterEqual(q.dexterity, 0)
        self.assertGreaterEqual(q.perception, 0)
        self.assertGreaterEqual(q.intelligence, 0)
        self.assertGreaterEqual(q.willpower, 0)

    def test_character_skill(self):
        """Character Skill"""
        q = qpCharacterSkill.objects.first()
        self.assertTrue(isinstance(q, qpCharacterSkill))
        self.assertTrue(isinstance(q.__str__(), str))
        self.assertEqual(q.__str__(), str(q.skill.name))
