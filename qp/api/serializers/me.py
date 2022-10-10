from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers

from qp.users.models import qpUserProfile
from qp.projects.models import qpProject

User = get_user_model()

class qpMeProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpProject
        fields = ["id", "name", "slug"]

class qpMeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, source="user.id")
    username = serializers.CharField(read_only=True, source="user.username")
    created_projects = qpMeProjectsSerializer(many=True, source="user.created_projects")
    owned_projects = qpMeProjectsSerializer(many=True, source="user.owned_projects")

    class Meta:
        model = qpUserProfile
        fields = ["id", "username", "name", "slug", "created_projects", "owned_projects"]
