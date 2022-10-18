from copy import deepcopy
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.users import qpUsersSimpleSerializer
from qp.forums.models import qpForum


class qpForumSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = qpForum
        fields = ["id", "name", "slug", "owner"]
        read_only_fields = ["id", "slug", "owner"]
    
    def get_owner(self, obj):
        if obj.owner:
            return qpUsersSimpleSerializer(obj.owner.profile).data
        return None


class qpForumCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = qpForum
        fields = ["id", "name", "owner"]
        read_only_fields = ["id", "owner"]
