from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class qpMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "profile")
