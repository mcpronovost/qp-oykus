from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAny, qpIsAuthenticated
from qp.rpg.models import qpRpgSkill
from qp.api.serializers.skills import qpSkillSerializer, qpSkillCreateSerializer


class qpSkillsListView(ListAPIView):
    """
    Skills GET list
    """
    permission_classes = [qpIsAny]
    queryset = qpRpgSkill.objects.all()
    serializer_class = qpSkillSerializer


class qpSkillsCreateView(CreateAPIView):
    """
    Skills CREATE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpRpgSkill.objects.all()
    serializer_class = qpSkillCreateSerializer

    def post(self, request, *args, **kwargs):
        rpg_pk = int(request.data.get("rpg"))
        rpg = request.user.owned_rpg.filter(
            pk=rpg_pk
        ).first()
        if rpg is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # ===---
        rpg_settings = rpg.get_settings()
        skills_count = rpg.skills.count()
        if skills_count >= rpg_settings.limit_skills:
            ctx = {
                "limit": rpg_settings.limit_skills,
                "count": skills_count
            }
            return Response(ctx, status=status.HTTP_429_TOO_MANY_REQUESTS)
        # ===---
        return self.create(request, *args, **kwargs)


class qpSkillsDetailView(RetrieveUpdateAPIView):
    """
    Races GET, UPDATE
    """
    permission_classes = [qpIsAny]
    queryset = qpRpgSkill.objects.all()
    serializer_class = qpSkillSerializer
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user is not None and user.is_authenticated and user.profile and instance.rpg.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpSkillsDeleteView(DestroyAPIView):
    """
    Races DELETE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpRpgSkill.objects.all()
    serializer_class = qpSkillSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.rpg.owner == self.request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)