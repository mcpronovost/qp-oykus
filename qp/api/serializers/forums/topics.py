from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from rest_framework import serializers

from qp.forums.models import qpForumTopic
from qp.api.serializers.characters import qpCharacterSimpleSerializer
from qp.api.serializers.forums.messages import qpForumMessageSerializer


class qpForumTopicSimpleSerializer(serializers.ModelSerializer):
    """
    Forum Topic simple serializer
    """
    author = serializers.SerializerMethodField()

    class Meta:
        model = qpForumTopic
        fields = ["id", "title", "forum", "category", "section", "author", "flag", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
    
    def get_author(self, obj):
        request = self.context.get("request")
        if obj.author is not None:
            return qpCharacterSimpleSerializer(obj.author, context={"request": request}).data
        return None


class qpForumTopicSerializer(serializers.ModelSerializer):
    """
    Forum Topic serializer
    """
    author = serializers.SerializerMethodField()
    messages = qpForumMessageSerializer(many=True)
    breadcrumb = serializers.SerializerMethodField()

    class Meta:
        model = qpForumTopic
        fields = ["id", "title", "forum", "category", "section", "author", "flag", "messages", "created_at", "updated_at", "breadcrumb"]
        read_only_fields = ["id", "created_at", "updated_at", "breadcrumb"]
    
    def get_author(self, obj):
        request = self.context.get("request")
        if obj.author is not None:
            return qpCharacterSimpleSerializer(obj.author, context={"request": request}).data
        return None
    
    def get_breadcrumb(self, obj):
        result = []
        slug = obj.forum.rpg.slug
        result.append({
            "name": str(obj.forum.rpg.name),
            "path": "/rpg/%s" % (
                str(slug)
            )
        })
        if obj.category:
            result.append({
                "name": str(obj.category.title),
                "path": "/rpg/%s/c%s-%s" % (
                    str(slug),
                    str(obj.category.pk),
                    str(slugify(obj.category.title))
                )
            })
        if obj.section:
            result.append({
                "name": str(obj.section.title),
                "path": "/rpg/%s/s%s-%s" % (
                    str(slug),
                    str(obj.section.pk),
                    str(slugify(obj.section.title))
                )
            })
        return result
