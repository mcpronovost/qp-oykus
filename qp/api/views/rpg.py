from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAny, qpIsAuthenticated
from qp.rpg.models import qpRpg
from qp.api.serializers.rpg import *


class qpRpgListView(ListAPIView):
    """
    RPG GET list
    """
    permission_classes = [qpIsAny]
    queryset = qpRpg.objects.all()
    serializer_class = qpRpgSerializer


class qpRpgCreateView(CreateAPIView):
    """
    RPG CREATE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpRpg.objects.all()
    serializer_class = qpRpgCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class qpRpgDetailView(RetrieveUpdateAPIView):
    """
    RPG GET, UPDATE
    """
    permission_classes = [qpIsAny]
    queryset = qpRpg.objects.all()
    serializer_class = qpRpgSerializer
    lookup_field = "slug"

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpRpgDeleteView(DestroyAPIView):
    """
    RPG DELETE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpRpg.objects.all()
    serializer_class = qpRpgSerializer
    lookup_field = "slug"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpRpgRacesListView(ListAPIView):
    """
    RPG Races GET list
    """
    permission_classes = [qpIsAny]
    serializer_class = qpRpgRaceSerializer

    def get_queryset(self):
        slug = str(self.kwargs["slug"])
        queryset = qpRpgRace.objects.filter(
            rpg__slug=slug
        )
        return queryset


class qpRpgSkillsListView(ListAPIView):
    """
    RPG Skills GET list
    """
    permission_classes = [qpIsAny]
    serializer_class = qpRpgSkillSerializer

    def get_queryset(self):
        slug = str(self.kwargs["slug"])
        queryset = qpRpgSkill.objects.filter(
            rpg__slug=slug
        )
        return queryset