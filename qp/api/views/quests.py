from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
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