from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAny, qpIsAuthenticated
from qp.rpg.models import qpRpg

from qp.api.serializers.rpg import qpRpgSerializer, qpRpgSimpleSerializer


class qpRpgListView(ListAPIView):
    """
    RPG `GET` list
    """
    permission_classes = [qpIsAny]
    queryset = qpRpg.objects.all()
    serializer_class = qpRpgSimpleSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class qpRpgDetailView(RetrieveUpdateDestroyAPIView):
    """
    RPG `GET`, `UPDATE`, `DELETE`
    """
    permission_classes = [qpIsAny]
    queryset = qpRpg.objects.all()
    serializer_class = qpRpgSerializer
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        # user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
