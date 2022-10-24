from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.users import qpUsersSimpleSerializer
from qp.rpg.models import *


class qpRpgSerializer(serializers.ModelSerializer):
    """
    Rpg serializer
    """
    owner = serializers.SerializerMethodField()

    class Meta:
        model = qpRpg
        fields = ["id", "name", "owner"]
        read_only_fields = ["id", "owner"]
    
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


class qpRpgRaceSerializer(serializers.ModelSerializer):
    """
    Rpg Race serializer
    """

    class Meta:
        model = qpRpgRace
        fields = ["id", "name"]
        read_only_fields = ["id"]


class qpRpgSkillSerializer(serializers.ModelSerializer):
    """
    Rpg Skill serializer
    """

    class Meta:
        model = qpRpgSkill
        fields = ["id", "name", "attribute"]
        read_only_fields = ["id"]