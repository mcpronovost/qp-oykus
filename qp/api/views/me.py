from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from django.contrib.auth import get_user_model

from qp.api.serializers.me import (
    qpMeSerializer,
    qpMeSettingsAccountUpdateSerializer,
    qpMeSettingsProfileUpdateSerializer
)

User = get_user_model()


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
