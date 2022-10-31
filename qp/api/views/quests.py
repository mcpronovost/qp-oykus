import math
import random
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAny, qpIsAuthenticated
from qp.quests.models import qpQuest, qpQuestLog
from qp.api.serializers.quests import qpQuestSerializer, qpQuestLogSerializer


class qpQuestsListView(ListAPIView):
    """
    Quests GET list
    """
    permission_classes = [qpIsAny]
    queryset = qpQuest.objects.all()
    serializer_class = qpQuestSerializer


class qpQuestsDetailView(RetrieveUpdateAPIView):
    """
    ``GET``,``UPDATE``: qpQuest
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpQuest.objects.all()
    serializer_class = qpQuestSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.rpg.owner == self.request.user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpQuestStartView(APIView):
    permission_classes = [qpIsAuthenticated]
    queryset = qpQuest.objects.all()
    serializer_class = qpQuestSerializer

    def post(self, request, *args, **kwargs):
        pk = int(kwargs["pk"])
        user_pk = request.POST.get("user", None)
        character_pk = request.POST.get("character", None)
        quest_pk = request.POST.get("quest", None)
        if user_pk is None or character_pk is None or quest_pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if int(pk) != int(quest_pk) or int(request.user.pk) != int(user_pk):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        quest = qpQuest.objects.filter(pk=pk).first()
        if quest is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        character = quest.section.characters.filter(
            pk=character_pk,
            user=request.user
        ).annotate(
            nb_logs=Count("questlogs", filter=Q(questlogs__is_completed=False))
        ).exclude(nb_logs__gt=0).first()
        if character is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # ===---
        qpQuestLog.objects.create(
            quest=quest,
            character=character,
            start=timezone.now(),
            end=timezone.now()+quest.duration
        )
        # ===---
        return Response(status=status.HTTP_200_OK)


class qpQuestEndView(APIView):
    permission_classes = [qpIsAuthenticated]
    queryset = qpQuest.objects.all()
    serializer_class = qpQuestSerializer

    def post(self, request, *args, **kwargs):
        pk = int(kwargs["pk"])
        user_pk = request.POST.get("user", None)
        character_pk = request.POST.get("character", None)
        quest_pk = request.POST.get("quest", None)
        questlog_pk = request.POST.get("questlog", None)
        if user_pk is None or character_pk is None or quest_pk is None or questlog_pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if int(pk) != int(quest_pk) or int(request.user.pk) != int(user_pk):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        quest = qpQuest.objects.filter(pk=pk).first()
        if quest is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        questlog = qpQuestLog.objects.filter(
            pk=questlog_pk,
            quest=quest,
            character__pk=character_pk
        ).first()
        if questlog is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # ===---
        is_success = False
        settings = quest.rpg.get_settings()
        character = questlog.character
        dm = settings.quest_malus_level_difference
        ql = quest.level
        qr_exp = quest.reward_exp
        at = settings.total_attribute
        qd = settings.quest_modifier_destiny
        for skill in quest.skills.all():
            character_skill, created = character.skills.get_or_create(skill=skill)
            sl = math.floor(1 if math.log2(character_skill.exp)-8 else math.log2(character_skill.exp)-8) if character_skill.exp else 0
            lm = (ql - sl) * dm
            sa = getattr(character, skill.attribute)
            ab = sa/at
            needed = (1-((ab-lm)-qd))
            rewards_currencies = {}
            reward_exp = 0
            if random.random() > needed:
                is_success = True
                reward_exp = qr_exp
                character_skill.exp = character_skill.exp + reward_exp
                rewards_currencies["exp"] = reward_exp
                for c in quest.reward_currencies.all():
                    amount = c.amount_min
                    if c.amount_max > c.amount_min:
                        amount = random.randint(c.amount_min, c.amount_max)
                    cc, _ = c.currency.characters_currencies.get_or_create(
                        character=character
                    )
                    cc.amount = cc.amount + amount
                    cc.save()
                    rewards_currencies[c.currency.icon] = amount
            else:
                if qr_exp > 0:
                    reward_exp = math.floor(qr_exp/2)
                    character_skill.exp = character_skill.exp + reward_exp
                    rewards_currencies["exp"] = reward_exp
            character_skill.save()
        # ===---
        questlog.is_completed = True
        questlog.is_success = is_success
        questlog.save()
        result = {
            "valid": True,
            "is_success": is_success,
            "rewards_currencies": rewards_currencies
        }
        # ===---
        return Response(result, status=status.HTTP_200_OK)


class qpQuestLogsListView(ListAPIView):
    """
    qpQuestLog GET list
    """
    permission_classes = [qpIsAny]
    serializer_class = qpQuestLogSerializer
    page_size = 32

    def get_queryset(self):
        pk = str(self.kwargs["pk"])
        queryset = qpQuestLog.objects.filter(
            quest__pk=pk
        )
        return queryset