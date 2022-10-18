from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAuthenticated
from qp.forums.models import qpForum
from qp.api.serializers.forums import *


class qpForumsView(ListAPIView):
    """
    Forums GET list
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForum.objects.all()
    serializer_class = qpForumSerializer


class qpForumsCreateView(CreateAPIView):
    """
    Forums CREATE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForum.objects.all()
    serializer_class = qpForumCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class qpForumsDetailView(RetrieveUpdateAPIView):
    """
    Forums GET, UPDATE
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForum.objects.all()
    serializer_class = qpForumSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
