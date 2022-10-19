from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from django.contrib.auth import get_user_model

from qp.api.serializers.me import (
    qpMeSerializer,
    qpMeSettingsAccountUpdateSerializer,
    qpMeSettingsProfileUpdateSerializer
)

User = get_user_model()


class qpPingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, fallback=None):
        if fallback:
            return Response(status=HTTP_404_NOT_FOUND)
        return Response({
            "valid": True
        })


class qpMeView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = qpMeSerializer

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeView : ", e)
        return None


class qpMeSettingsAccountUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = qpMeSettingsAccountUpdateSerializer

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeSettingsAccountUpdateView : ", e)
        return None


class qpMeSettingsProfileUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = qpMeSettingsProfileUpdateSerializer

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeSettingsProfileUpdateView : ", e)
        return None
