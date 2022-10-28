from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.characters.models import qpCharacter
from qp.api.serializers.users import qpUsersSimpleSerializer
from qp.api.serializers.rpg import qpRpgSimpleSerializer


class qpCharacterSimpleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    rpg = serializers.SerializerMethodField()

    class Meta:
        model = qpCharacter
        fields = ["id", "user", "rpg", "first_name", "middle_name", "last_name", "name", "initial"]
        read_only_fields = ["id", "user", "name", "initial"]
    
    def get_user(self, obj):
        if obj.user:
            return qpUsersSimpleSerializer(obj.user.profile).data
        return None
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
        return None


class qpCharacterSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    rpg = serializers.SerializerMethodField()
    resistances = serializers.SerializerMethodField()
    attributes = serializers.SerializerMethodField()

    class Meta:
        model = qpCharacter
        fields = ["id", "user", "rpg", "first_name", "middle_name", "last_name", "name", "initial", "resistances", "attributes"]
        read_only_fields = ["id", "user", "name", "initial", "resistances", "attributes"]
    
    def get_user(self, obj):
        if obj.user:
            return qpUsersSimpleSerializer(obj.user.profile).data
        return None
    
    def get_rpg(self, obj):
        if obj.rpg:
            return qpRpgSimpleSerializer(obj.rpg).data
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


class qpCharacterCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = qpCharacter
        fields = ["id", "user", "rpg", "first_name", "middle_name", "last_name"]
        read_only_fields = ["id", "user"]