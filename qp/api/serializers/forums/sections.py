from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from rest_framework import serializers

from qp.api.serializers.characters import qpCharacterSimpleSerializer
from qp.api.serializers.forums.topics import qpForumTopicSimpleSerializer
from qp.forums.models import qpForumSection


class qpForumSectionSerializer(serializers.ModelSerializer):
    """
    Forum Section serializer
    """
    category = serializers.SerializerMethodField()
    topics = qpForumTopicSimpleSerializer(many=True)
    breadcrumb = serializers.SerializerMethodField()

    class Meta:
        model = qpForumSection
        fields = ["id", "title", "description", "forum", "category", "topics", "breadcrumb"]
        read_only_fields = ["id", "category", "breadcrumb"]
    
    def get_category(self, obj):
        result = {
            "id": int(obj.category.pk),
            "title": str(obj.category.title),
            "slug": slugify(obj.category.title)
        }
        return result
    
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
        return result


class qpForumSectionSimpleSerializer(serializers.ModelSerializer):
    """
    Forum Category's Section serializer
    """
    last_topic = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = qpForumSection
        fields = ["id", "title", "forum", "category", "width", "last_topic", "last_message"]
        read_only_fields = ["id"]
    
    def get_last_topic(self, obj):
        result = None
        last_message = obj.get_last_message()
        if last_message is not None:
            last_topic = last_message.topic
            result = {
                "id": last_topic.pk,
                "title": str(last_topic.title),
                "updated_at": last_message.created_at
            }
        return result
    
    def get_last_message(self, obj):
        request = self.context.get("request")
        result = None
        last_message = obj.get_last_message()
        if last_message is not None:
            result = {
                "id": last_message.pk,
                "title": str(last_message.topic.title),
                "author": qpCharacterSimpleSerializer(last_message.author, context={"request": request}).data,
                "created_at": last_message.created_at,
                "topic": {
                    "id": int(last_message.topic.id),
                    "title": str(last_message.topic.title)
                }
            }
        return result
