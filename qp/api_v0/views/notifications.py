from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from qp.notifications.models import qpNotification
from qp.api.serializers.notifications import qpNotificationSeenSerializer

User = get_user_model()

class qpNotificationsSeenView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = qpNotification.objects.all()
    serializer_class = qpNotificationSeenSerializer
    lookup_field = "pk"

    def get_queryset(self):
        queryset = super(qpNotificationsSeenView, self).get_queryset()
        queryset.filter(user_to=self.request.user)
        return queryset

    def perform_update(self, serializer):
        serializer.save(is_seen=True)

class qpNotificationsAllSeenView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = qpNotification.objects.all()
    serializer_class = qpNotificationSeenSerializer

    def patch(self, request, *args, **kwargs):
        instances = qpNotification.objects.filter(
          user_to=self.request.user,
          is_seen=False
        )
        instances.update(is_seen=True)
        serializer = qpNotificationSeenSerializer(instances, many=True)
        return Response(serializer.data)
