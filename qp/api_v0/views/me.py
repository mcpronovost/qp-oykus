from qp.api.permissions import qpIsAny, qpIsAuthenticated
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from django.contrib.auth import get_user_model

from qp.api.serializers.me import qpMeSerializer
from qp.api.serializers.me import qpMeSettingsAccountUpdateSerializer, qpMeSettingsProfileUpdateSerializer
from qp.api.serializers.rpg import qpRpgSimpleSerializer
from qp.api.serializers.characters import qpCharacterSimpleSerializer

User = get_user_model()


class qpPingView(APIView):
    permission_classes = [qpIsAny]

    def get(self, request, fallback=None):
        if fallback:
            return Response(status=HTTP_404_NOT_FOUND)
        return Response({
            "valid": True
        })


class qpMeView(RetrieveAPIView):
    permission_classes = [qpIsAuthenticated]
    queryset = User.objects.all()
    serializer_class = qpMeSerializer

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeView : ", e)
        return None


class qpMeSettingsAccountUpdateView(UpdateAPIView):
    permission_classes = [qpIsAuthenticated]
    queryset = User.objects.all()
    serializer_class = qpMeSettingsAccountUpdateSerializer

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeSettingsAccountUpdateView : ", e)
        return None


class qpMeSettingsProfileUpdateView(UpdateAPIView):
    permission_classes = [qpIsAuthenticated]
    queryset = User.objects.all()
    serializer_class = qpMeSettingsProfileUpdateSerializer

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeSettingsProfileUpdateView : ", e)
        return None


class qpMeRpgListView(ListAPIView):
    """
    Me RPG GET list
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpRpgSimpleSerializer

    def get_queryset(self):
        queryset = self.request.user.owned_rpg.all()
        return queryset


class qpMeCharactersListView(ListAPIView):
    """
    Me Characters GET list
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpCharacterSimpleSerializer

    def get_queryset(self):
        queryset = self.request.user.characters.all()
        return queryset
