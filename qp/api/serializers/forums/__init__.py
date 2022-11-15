from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.users import qpUsersSimpleSerializer
from qp.api.serializers.forums.categories import qpForumCategorySerializer
from qp.forums.models import qpForum


class qpForumSerializer(serializers.ModelSerializer):
    """
    Forum serializer
    """
    owner = serializers.SerializerMethodField()
    categories = qpForumCategorySerializer(many=True)

    class Meta:
        model = qpForum
        fields = ["id", "owner", "categories"]
        read_only_fields = ["id", "owner", "categories"]
    
    def get_owner(self, obj):
        if obj.rpg and obj.rpg.owner:
            return qpUsersSimpleSerializer(obj.rpg.owner.profile).data
        return None
