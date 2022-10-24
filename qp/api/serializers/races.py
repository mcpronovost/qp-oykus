from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.rpg.models import *


class qpRaceSerializer(serializers.ModelSerializer):
    """
    Race serializer
    """

    class Meta:
        model = qpRpgRace
        fields = ["id", "rpg", "name", "description"]
        read_only_fields = ["id"]


class qpRaceCreateSerializer(serializers.ModelSerializer):
    """
    Race serializer
    """

    class Meta:
        model = qpRpgRace
        fields = ["id", "rpg", "name", "description"]
        read_only_fields = ["id"]