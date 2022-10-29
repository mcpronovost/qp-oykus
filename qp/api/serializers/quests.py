from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.quests.models import qpQuest, qpQuestLog
from qp.api.serializers.rpg import qpRpgSimpleSerializer
from qp.api.serializers.characters import qpCharacterSimpleSerializer


class qpQuestSimpleSerializer(serializers.ModelSerializer):
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpQuest
        fields = ["id", "rpg", "title", "description"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpQuestSerializer(serializers.ModelSerializer):
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpQuest
        fields = ["id", "rpg", "title", "description"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpQuestLogSerializer(serializers.ModelSerializer):
    quest = serializers.SerializerMethodField()
    character = serializers.SerializerMethodField()

    class Meta:
        model = qpQuestLog
        fields = ["id", "quest", "character", "start", "end", "is_completed", "is_success"]
        read_only_fields = ["id"]
    
    def get_quest(self, obj):
        if obj.quest:
            return qpQuestSimpleSerializer(obj.quest).data
        return None
    
    def get_character(self, obj):
        if obj.character:
            return qpCharacterSimpleSerializer(obj.character).data
        return None