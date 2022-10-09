from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import get_user_model

from qp.api.serializers.me import qpMeSerializer

User = get_user_model()


class qpMeView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = qpMeSerializer
    lookup_field = "pk"

    def get_object(self):
        try:
            return self.request.user.profile
        except Exception as e:
            print("Error on qpMeView : ", e)
        return None
