from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from qp.users.models import qpUserProfile

User = get_user_model()


class qpUsersSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source="user.id")

    class Meta:
        model = qpUserProfile
        fields = ["id", "name", "slug", "initial", "avatar"]