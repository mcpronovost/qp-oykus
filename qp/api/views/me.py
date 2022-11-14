from qp.api.permissions import qpIsAny, qpIsAuthenticated
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from django.contrib.auth import get_user_model

from qp.api.serializers.me import qpMeSerializer

User = get_user_model()


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
