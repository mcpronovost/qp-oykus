from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.projects.models import qpProject

class qpProjectsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpProject
        fields = ["id", "slug", "name", "caption", "description", "primary_color", "creator", "owner"]
        read_only_fields = ["id", "slug"]
