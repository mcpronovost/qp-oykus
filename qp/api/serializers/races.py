from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.rpg.models import qpRpgRace
from qp.api.serializers.rpg import qpRpgSimpleSerializer


class qpRaceSimpleSerializer(serializers.ModelSerializer):
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpRpgRace
        fields = ["id", "rpg", "name", "name_male", "name_female", "description"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpRaceSerializer(serializers.ModelSerializer):
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpRpgRace
        fields = ["id", "rpg", "name", "name_male", "name_female", "description"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpRaceCreateSerializer(serializers.ModelSerializer):
    """
    Race serializer
    """

    class Meta:
        model = qpRpgRace
        fields = ["id", "rpg", "name", "description"]
        read_only_fields = ["id"]