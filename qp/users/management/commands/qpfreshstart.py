from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from qp.rpg.models import qpRpg, qpRpgRace, qpRpgSkill, qpRpgCurrency, qpRpgStyle, qpSettingsRpg
from qp.quests.models import qpQuest, qpQuestRewardCurrency, qpQuestLog
from qp.notifications.models import qpNotification
from qp.forums.models import qpForum, qpForumCategory, qpForumSection, qpForumTopic, qpForumMessage, qpForumTrackSection, qpForumTrackTopic
from qp.characters.models import qpCharacter, qpCharacterSkill, qpCharacterCurrency

User = get_user_model()

class Command(BaseCommand):
    help = "Clean db and create a fresh start."

    def handle(self, *args, **options):
        print("--- Start ``Clean db and create a fresh start`` --------------")
        print("---")
        self.clean_rpg()
        self.clean_quests()
        self.clean_notifications()
        self.clean_forums()
        self.clean_characters()
        self.clean_users()
        print("---")
        self.create_default()
        print("---")
        print("--- End ``Clean db and create a fresh start`` ----------------")
    
    def clean_rpg(self):
        for o in qpRpg.objects.all():
            print("Delete ``RPG`` ................... ", str(o))
            o.delete()
        for o in qpRpgRace.objects.all():
            print("Delete ``RPG Race`` .............. ", str(o))
            o.delete()
        for o in qpRpgSkill.objects.all():
            print("Delete ``RPG Skill`` ............. ", str(o))
            o.delete()
        for o in qpRpgCurrency.objects.all():
            print("Delete ``RPG Currency`` .......... ", str(o))
            o.delete()
        for o in qpRpgStyle.objects.all():
            print("Delete ``RPG Style`` ............. ", str(o))
            o.delete()
        for o in qpSettingsRpg.objects.all():
            print("Delete ``RPG Settings`` .......... ", str(o))
            o.delete()
    
    def clean_quests(self):
        for o in qpQuest.objects.all():
            print("Delete ``Quest`` ", str(o))
            o.delete()
        for o in qpQuestRewardCurrency.objects.all():
            print("Delete ``Quest Reward Currency`` ", str(o))
            o.delete()
        for o in qpQuestLog.objects.all():
            print("Delete ``Quest Log`` ", str(o))
            o.delete()
    
    def clean_notifications(self):
        for o in qpNotification.objects.all():
            print("Delete ``Notification`` ", str(o))
            o.delete()

    def clean_forums(self):
        for o in qpForum.objects.all():
            print("Delete ``Forum`` ", str(o))
            o.delete()
        for o in qpForumCategory.objects.all():
            print("Delete ``Forum Category`` ", str(o))
            o.delete()
        for o in qpForumSection.objects.all():
            print("Delete ``Forum Section`` ", str(o))
            o.delete()
        for o in qpForumTopic.objects.all():
            print("Delete ``Forum Topic`` ", str(o))
            o.delete()
        for o in qpForumMessage.objects.all():
            print("Delete ``Forum Message`` ", str(o))
            o.delete()
        for o in qpForumTrackSection.objects.all():
            print("Delete ``Forum Track Section`` ", str(o))
            o.delete()
        for o in qpForumTrackTopic.objects.all():
            print("Delete ``Forum Track Topic`` ", str(o))
            o.delete()

    def clean_characters(self):
        for o in qpCharacter.objects.all():
            print("Delete ``Character`` ", str(o))
            o.delete()
        for o in qpCharacterSkill.objects.all():
            print("Delete ``Character Skill`` ", str(o))
            o.delete()
        for o in qpCharacterCurrency.objects.all():
            print("Delete ``Character Currency`` ", str(o))
            o.delete()

    def clean_users(self):
        for o in User.objects.filter(is_superuser=False):
            print("Delete ``User`` ", str(o))
            o.delete()

    def create_default(self):
        settings = qpSettingsRpg.objects.create()
        print("Create ``RPG Settings`` .......... ", str(settings))
        rpg = qpRpg.objects.create(name="Oykus")
        print("Create ``RPG`` ................... ", str(rpg))
        rpg_settings = qpSettingsRpg.objects.create(rpg=rpg)
        print("Create ``RPG Settings`` .......... ", str(rpg_settings))
        forum = qpForum.objects.create(rpg=rpg)
        print("Create ``Forum`` ................. ", str(forum))
        forum_category = qpForumCategory.objects.create(forum=forum, title="Ma première catégorie")
        print("Create ``Forum Category`` ........ ", str(forum_category))
        forum_section = qpForumSection.objects.create(forum=forum, category=forum_category, title="Ma première section")
        print("Create ``Forum Section`` ......... ", str(forum_section))
