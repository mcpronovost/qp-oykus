from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from qp.users.models import qpUserProfile
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
        user = User.objects.create_user("oykus", "admin@oykus.ca", "testmdp123")
        qpUserProfile.objects.create(user=user, name="Oykus")
        print("Create ``User`` .......... ", str(user))
        settings = qpSettingsRpg.objects.create()
        print("Create ``RPG Settings`` .......... ", str(settings))
        rpg = qpRpg.objects.create(name="Oykus", creator=user, owner=user)
        print("Create ``RPG`` ................... ", str(rpg))
        rpg_settings = qpSettingsRpg.objects.create(rpg=rpg)
        print("Create ``RPG Settings`` .......... ", str(rpg_settings))
        character = qpCharacter.objects.create(user=user, rpg=rpg, first_name="Oykus")
        print("Create ``Character`` .......... ", str(character))
        forum = qpForum.objects.create(rpg=rpg)
        print("Create ``Forum`` ................. ", str(forum))
        forum_category = qpForumCategory.objects.create(forum=forum, title="Ma première catégorie")
        print("Create ``Forum Category`` ........ ", str(forum_category))
        forum_section = qpForumSection.objects.create(forum=forum, category=forum_category, title="Ma première section")
        print("Create ``Forum Section`` ......... ", str(forum_section))
        forum_topic = qpForumTopic.objects.create(forum=forum, category=forum_category, section=forum_section, author=character, title="Mon premier sujet")
        print("Create ``Forum Topic`` ......... ", str(forum_topic))
        forum_message = qpForumMessage.objects.create(forum=forum, category=forum_category, section=forum_section, topic=forum_topic, author=character, content="Ceci est mon premier message.\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Donec metus turpis, ullamcorper in ipsum ut, pulvinar mollis ipsum. Sed dictum quis nisi in sollicitudin. Integer porttitor nisi magna, nec tincidunt ante mattis sed. Etiam ultricies nec arcu sit amet tincidunt. Morbi sem orci, facilisis id finibus ac, finibus et turpis. Integer hendrerit eu est at facilisis. Ut sit amet nibh imperdiet, tristique tortor at, finibus libero.\nVestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vestibulum dapibus cursus est sed rutrum.\n\nProin suscipit risus non tortor pretium, eu pellentesque felis ullamcorper. Nunc eleifend ligula sit amet felis semper tincidunt. Duis suscipit massa arcu, vitae placerat massa interdum quis. Nullam sit amet augue at mauris faucibus aliquam. Cras quis eros velit. Praesent volutpat urna et ex suscipit, ac fermentum dui venenatis. Sed efficitur, mi nec posuere ultrices, neque neque tristique ante, in accumsan odio nisi ac nisi. Aliquam elementum sodales felis non aliquam. Nunc tempor venenatis mi, eget finibus urna faucibus quis.\n\nPellentesque sed vehicula urna. Donec iaculis libero in dui tristique, a vehicula quam posuere. Duis dictum nisl at commodo posuere. Maecenas quis est quis augue semper consectetur. Proin finibus, diam eu placerat feugiat, diam ante consequat odio, sed gravida ligula massa a turpis. Proin nec ex ex. Donec vulputate nisi quis facilisis finibus. Nullam urna dolor, pharetra ac leo id, blandit dapibus augue. Nulla facilisi. Proin nec magna orci. Praesent ac arcu nec lacus tempor porttitor.\n\nAliquam facilisis semper leo nec tempus. In consequat elit sed tellus pulvinar tristique in et mauris. Donec vel sem eget ligula convallis sodales. Mauris sed auctor magna. Proin ipsum odio, vehicula nec leo ut, elementum viverra mauris. Curabitur in eros ut lectus venenatis lacinia. Nulla et diam consectetur, auctor ligula id, vulputate magna. Donec orci dui, vulputate quis nisl et, tincidunt pulvinar lacus.\n\nProin et magna tempor, interdum leo sit amet, laoreet ligula. Nullam quis commodo massa.\nFusce lacinia facilisis erat, sit amet dapibus erat elementum a.\nInteger gravida sit amet enim a consequat. Etiam quis vulputate augue. Etiam pharetra enim nec odio tincidunt, id egestas arcu ultrices. Suspendisse turpis nibh, pulvinar at sem vitae, commodo mollis tortor. Proin quis justo feugiat, accumsan massa ut, suscipit purus. Curabitur hendrerit, purus sit amet bibendum laoreet, neque ligula fringilla magna, varius efficitur sapien ipsum non magna. In pretium malesuada mauris at varius. Maecenas ut porta dolor.\nVivamus bibendum quam odio, luctus ultrices augue commodo sit amet.")
        print("Create ``Forum Message`` ......... ", str(forum_message))
