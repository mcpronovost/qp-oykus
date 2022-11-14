from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.rpg.models import qpRpgSkill
from qp.api.serializers.rpg import qpRpgSimpleSerializer


class qpSkillSimpleSerializer(serializers.ModelSerializer):
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpRpgSkill
        fields = ["id", "rpg", "name", "attribute", "description"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpSkillSerializer(serializers.ModelSerializer):
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpRpgSkill
        fields = ["id", "rpg", "name", "attribute", "description"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpSkillCreateSerializer(serializers.ModelSerializer):
    """
    Skill serializer
    """

    class Meta:
        model = qpRpgSkill
        fields = ["id", "rpg", "name", "attribute", "description"]
        read_only_fields = ["id"]