from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAny, qpIsAuthenticated
from qp.rpg.models import qpRpg
from qp.characters.models import qpCharacter
from qp.api.serializers.characters import qpCharacterSerializer, qpCharacterCreateSerializer


class qpCharactersListView(ListAPIView):
    """
    Characters GET list
    """
    permission_classes = [qpIsAny]
    queryset = qpCharacter.objects.all()
    serializer_class = qpCharacterSerializer


class qpCharactersCreateView(CreateAPIView):
    """
    Characters CREATE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpCharacter.objects.all()
    serializer_class = qpCharacterCreateSerializer

    def post(self, request, *args, **kwargs):
        rpg_pk = int(request.data.get("rpg"))
        rpg = qpRpg.objects.filter(pk=rpg_pk).first()
        if rpg is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # ===---
        rpg_settings = rpg.get_settings()
        characters_count = rpg.characters.count()
        if characters_count >= rpg_settings.limit_characters:
            ctx = {
                "limit": rpg_settings.limit_characters,
                "count": characters_count
            }
            return Response(ctx, status=status.HTTP_429_TOO_MANY_REQUESTS)
        # ===---
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class qpCharactersDetailView(RetrieveUpdateAPIView):
    """
    Characters GET, UPDATE
    """
    permission_classes = [qpIsAny]
    queryset = qpCharacter.objects.all()
    serializer_class = qpCharacterSerializer
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user is not None and user.is_authenticated and user.profile and instance.user == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpCharactersDeleteView(DestroyAPIView):
    """
    Characters DELETE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpCharacter.objects.all()
    serializer_class = qpCharacterSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == self.request.user or instance.rpg.owner == self.request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)