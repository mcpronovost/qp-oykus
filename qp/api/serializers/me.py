from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers

from qp.users.models import qpUserProfile
from qp.rpg.models import qpRpg
from qp.characters.models import qpCharacter
from qp.notifications.models import qpNotification

User = get_user_model()


class qpMeqpNotificationsSerializer(serializers.ModelSerializer):
    initial = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    class Meta:
        model = qpNotification
        fields = ["id", "user_from", "initial", "icon", "content", "has_type"]
    
    def get_initial(self, obj):
        if obj.user_from:
            return str(obj.user_from.profile.initial)
        return None
    
    def get_icon(self, obj):
        request = self.context["request"]
        if obj.user_from:
            return None
        return None


class qpMeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source="user.id")
    username = serializers.CharField(read_only=True, source="user.username")
    email = serializers.CharField(read_only=True, source="user.email")
    notifications = serializers.SerializerMethodField()

    class Meta:
        model = qpUserProfile
        fields = ["id", "username", "email", "name", "initial", "slug", "lang", "timezone", "avatar", "notifications"]
    
    def get_notifications(self, obj):
        results = qpNotification.objects.filter(user_to=obj.user, is_seen=False)[0:12]
        return qpMeqpNotificationsSerializer(results, many=True, context={"request": self.context["request"]}).data

class qpMeSettingsAccountUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpUserProfile
        fields = ["lang", "timezone"]

class qpMeSettingsProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpUserProfile
        fields = ["name", "avatar"]
