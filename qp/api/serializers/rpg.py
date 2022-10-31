from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.rpg.models import qpRpg
from qp.api.serializers.users import qpUsersSimpleSerializer


class qpRpgSimpleSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = qpRpg
        fields = ["id", "name", "initial", "slug", "owner", "caption", "primary_color", "icon", "forum"]
        read_only_fields = ["id", "name", "initial", "slug", "owner", "caption", "primary_color", "icon", "forum"]
    
    def get_owner(self, obj):
        if obj.owner:
            return qpUsersSimpleSerializer(obj.owner.profile).data
        return None


class qpRpgSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = qpRpg
        fields = ["id", "name", "initial", "slug", "owner", "caption", "primary_color", "icon", "forum"]
        read_only_fields = ["id", "initial", "owner", "forum"]
    
    def get_owner(self, obj):
        if obj.owner:
            return qpUsersSimpleSerializer(obj.owner.profile).data
        return None


class qpRpgCreateSerializer(serializers.ModelSerializer):
    """
    Rpg ``create`` serializer
    """

    class Meta:
        model = qpRpg
        fields = ["id", "name", "owner"]
        read_only_fields = ["id", "owner"]
