from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND


class qpPingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, fallback=None):
        if fallback:
            return Response(status=HTTP_404_NOT_FOUND)
        return Response({
            "valid": True
        })