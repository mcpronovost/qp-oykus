from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.forums.sections import qpForumSectionSimpleSerializer
from qp.forums.models import qpForumCategory


class qpForumCategorySerializer(serializers.ModelSerializer):
    """
    Forum Category serializer
    """
    sections = qpForumSectionSimpleSerializer(many=True)
    breadcrumb = serializers.SerializerMethodField()

    class Meta:
        model = qpForumCategory
        fields = ["id", "title", "forum", "sections", "breadcrumb"]
        read_only_fields = ["id", "breadcrumb"]
    
    def get_breadcrumb(self, obj):
        result = []
        slug = obj.forum.rpg.slug
        result.append({
            "name": str(obj.forum.rpg.name),
            "path": "/rpg/%s" % (
                str(slug)
            )
        })
        return result
