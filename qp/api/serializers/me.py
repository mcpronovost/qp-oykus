from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers

from qp.users.models import qpUserProfile
from qp.projects.models import qpProject
from qp.notifications.models import qpNotification

User = get_user_model()


class qpMeProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpProject
        fields = ["id", "name", "slug", "initial", "primary_color", "icon"]


class qpMeqpNotificationsSerializer(serializers.ModelSerializer):
    initial = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    class Meta:
        model = qpNotification
        fields = ["id", "user_from", "project_from", "initial", "icon", "content", "has_type"]
    
    def get_initial(self, obj):
        if obj.user_from:
            return str(obj.user_from.profile.initial)
        elif obj.project_from:
            return str(obj.project_from.initial)
        return None
    
    def get_icon(self, obj):
        request = self.context["request"]
        if obj.user_from:
            return None
        elif obj.project_from and obj.project_from.icon:
            return request.build_absolute_uri(obj.project_from.icon.url)
        return None


class qpMeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source="user.id")
    username = serializers.CharField(read_only=True, source="user.username")
    email = serializers.CharField(read_only=True, source="user.email")
    owned_projects = qpMeProjectsSerializer(many=True, source="user.owned_projects")
    notifications = serializers.SerializerMethodField()

    class Meta:
        model = qpUserProfile
        fields = ["id", "username", "email", "name", "initial", "slug", "lang", "timezone", "avatar", "owned_projects", "notifications"]
    
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
