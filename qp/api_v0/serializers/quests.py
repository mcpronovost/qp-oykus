import math
from django.utils.translation import gettext_lazy as _
from django.db.models import Count, Q
from rest_framework import serializers

from qp.characters.models import qpCharacter
from qp.forums.models import qpForumSection
from qp.quests.models import qpQuest, qpQuestLog
from qp.api.serializers.rpg import qpRpgSimpleSerializer
from qp.api.serializers.characters import qpCharacterSimpleSerializer, qpCharacterSerializer


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
    section = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    reward_currencies = serializers.SerializerMethodField()
    characters = serializers.SerializerMethodField()
    current = serializers.SerializerMethodField()

    class Meta:
        model = qpQuest
        fields = ["id", "rpg", "section", "title", "description", "skills", "reward_exp", "reward_currencies", "characters", "current"]
        read_only_fields = ["id"]
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None
    
    def get_section(self, obj):
        if obj.section:
            result = obj.section
            return {
                "id": result.pk,
                "title": result.title,
                "categorie": result.category.title
            }
        return None
    
    def get_skills(self, obj):
        result = []
        for s in obj.skills.all():
            result.append(s.pk)
        return result
    
    def get_reward_currencies(self, obj):
        result = []
        for c in obj.reward_currencies.all():
            if (c.amount_min > 0) or (c.amount_max > 0):
                result.append({
                    "name": str(c.currency.name),
                    "icon": str(c.currency.icon),
                    "amount_min": int(c.amount_min) if c.amount_max > c.amount_min else int(c.amount_max),
                    "amount_max": int(c.amount_max) if c.amount_max > c.amount_min else int(c.amount_min)
                })
        return result
    
    def get_characters(self, obj):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            characters = obj.section.characters.filter(user=request.user).annotate(nb_logs=Count("questlogs", filter=Q(questlogs__is_completed=False))).exclude(nb_logs__gt=0)
            return qpCharacterSerializer(characters, many=True, context={"request": request}).data
        return []
    
    def get_current(self, obj):
        request = self.context.get("request")
        result = qpQuestLog.objects.filter(
            quest=obj,
            is_completed=False
        ).first()
        if result is not None:
            return {
                "id": result.pk,
                "character": qpCharacterSerializer(result.character, context={"request": request}).data,
                "start": result.start,
                "end": result.end
            }
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