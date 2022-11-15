from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.characters import qpCharacterSimpleSerializer
from qp.forums.models import qpForumMessage

class qpForumMessageSerializer(serializers.ModelSerializer):
    """
    Forum Message serializer
    """
    author = serializers.SerializerMethodField()

    class Meta:
        model = qpForumMessage
        fields = ["id", "forum", "category", "section", "topic", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
    
    def get_author(self, obj):
        request = self.context.get("request")
        if obj.author is not None:
            return qpCharacterSimpleSerializer(obj.author, context={"request": request}).data
        return None