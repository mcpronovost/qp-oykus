from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.users import qpUsersSimpleSerializer

from qp.projects.models import qpProject


class qpProjectsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpProject
        fields = ["id", "slug", "name", "caption", "description", "primary_color", "creator", "owner"]
        read_only_fields = ["id", "slug"]


class qpProjectsDetailSerializer(serializers.ModelSerializer):
    owner = qpUsersSimpleSerializer(source="owner.profile")

    class Meta:
        model = qpProject
        fields = ["id", "slug", "name", "initial", "caption", "description", "primary_color", "owner"]
        read_only_fields = ["id", "slug", "name", "initial", "caption", "description", "primary_color", "owner"]


class qpProjectsDetailOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpProject
        fields = ["id", "slug", "name", "initial", "caption", "description", "primary_color", "creator", "owner", "created_at",]
        read_only_fields = ["id", "slug"]
