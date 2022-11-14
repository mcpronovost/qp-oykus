import math
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.characters.models import qpCharacter
from qp.api.serializers.users import qpUsersSimpleSerializer
from qp.api.serializers.rpg import qpRpgSimpleSerializer
from qp.api.serializers.races import qpRaceSimpleSerializer


class qpCharacterSimpleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    rpg = serializers.SerializerMethodField()
    race = serializers.SerializerMethodField()

    class Meta:
        model = qpCharacter
        fields = ["id", "user", "rpg", "first_name", "middle_name", "last_name", "name", "initial", "gender", "race", "avatar"]
        read_only_fields = ["id", "user", "name", "initial"]
    
    def get_user(self, obj):
        request = self.context.get("request")
        if obj.user:
            return qpUsersSimpleSerializer(obj.user.profile, context={"request": request}).data
        return None
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None
    
    def get_race(self, obj):
        if obj.race:
            result = qpRaceSimpleSerializer(obj.race).data
            if obj.gender == "male" and result["name_male"] is not None:
                return result["name_male"]
            elif obj.gender == "female" and result["name_female"] is not None:
                return result["name_female"]
            return result["name"]
        return None


class qpCharacterSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    rpg = serializers.SerializerMethodField()
    race = serializers.SerializerMethodField()
    resistances = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    wallet = serializers.SerializerMethodField()

    class Meta:
        model = qpCharacter
        fields = ["id", "user", "rpg", "first_name", "middle_name", "last_name", "name", "initial", "gender", "race", "avatar", "resistances", "attributes", "skills", "wallet"]
        read_only_fields = ["id", "user", "name", "initial", "resistances", "attributes", "skills", "wallet"]
    
    def get_user(self, obj):
        request = self.context.get("request")
        if obj.user:
            return qpUsersSimpleSerializer(obj.user.profile, context={"request": request}).data
        return None
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None
    
    def get_race(self, obj):
        if obj.race:
            result = qpRaceSimpleSerializer(obj.race).data
            if obj.gender == "male" and result["name_male"] is not None:
                return result["name_male"]
            elif obj.gender == "female" and result["name_female"] is not None:
                return result["name_female"]
            return result["name"]
        return None
    
    def get_resistances(self, obj):
        result = {
            "physical": obj.physical,
            "mental": obj.mental,
            "spiritual": obj.spiritual
        }
        return result
    
    def get_attributes(self, obj):
        result = {
            "strength": obj.strength,
            "constitution": obj.constitution,
            "dexterity": obj.dexterity,
            "perception": obj.perception,
            "intelligence": obj.intelligence,
            "willpower": obj.willpower
        }
        return result
    
    def get_skills(self, obj):
        result = {}
        for s in obj.skills.all():
            level = math.floor(1 if math.log2(s.exp)-8 else math.log2(s.exp)-8) if s.exp else 0
            result[s.skill.pk] = {
                "id": s.pk,
                "name": s.skill.name,
                "exp": s.exp,
                "level": level,
                "next": math.pow(2, level+9)
            }
        return result
    
    def get_wallet(self, obj):
        result = obj.get_wallet()
        return result


class qpCharacterCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = qpCharacter
        fields = ["id", "user", "rpg", "first_name", "middle_name", "last_name"]
        read_only_fields = ["id", "user"]