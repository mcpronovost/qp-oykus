import math
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
            end=timezone.now()+timezone.timedelta(seconds=10)
        )
        # ===---
        return Response(status=status.HTTP_200_OK)


class qpQuestEndView(APIView):
    permission_classes = [qpIsAuthenticated]
    queryset = qpQuest.objects.all()
    serializer_class = qpQuestSerializer

    def post(self, request, *args, **kwargs):
        print("-------------------------- end")
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
        # ===--- todo: donner les rewards
        character = questlog.character
        is_success = False
        quest_level = quest.level
        for skill in quest.skills.all():
            print("quest_level : ", quest_level)
            print("character skill : ", "-")
            print("level difference : ", "-")
            print("difference points : ", "-")
            
            points = 4097
            print("level : ", math.floor((math.sqrt(((points / 1024) * 8) + 1) - 1) / 2) + 1)
            print(skill.attribute)
            print("character attribute : ", getattr(character, skill.attribute))
        # ===---
        questlog.is_completed = True
        questlog.is_success = is_success
        #questlog.save()
        result = {
            "is_success": is_success
        }
        # ===---
        return Response(result, status=status.HTTP_200_OK)


class qpQuestLogsListView(ListAPIView):
    """
    qpQuestLog GET list
    """
    permission_classes = [qpIsAny]
    serializer_class = qpQuestLogSerializer

    def get_queryset(self):
        pk = str(self.kwargs["pk"])
        queryset = qpQuestLog.objects.filter(
            quest__pk=pk
        )
        return queryset