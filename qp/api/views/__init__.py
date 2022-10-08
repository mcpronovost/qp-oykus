from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class qpPingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "valid": True
        })