from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from rest_framework import serializers

from qp.api.serializers.users import qpUsersSimpleSerializer
from qp.api.serializers.characters import qpCharacterSimpleSerializer
from qp.forums.models import *


class qpMessageSerializer(serializers.ModelSerializer):
    """
    Forum Message serializer
    """

    class Meta:
        model = qpForumMessage
        fields = ["id", "content", "forum", "category", "section", "topic"]
        read_only_fields = ["id"]


class qpMessageCreateSerializer(serializers.ModelSerializer):
    """
    Forum Message serializer
    """

    class Meta:
        model = qpForumMessage
        fields = ["id", "content", "topic"]
        read_only_fields = ["id"]


class qpTopicSerializer(serializers.ModelSerializer):
    """
    Forum Topic serializer
    """

    class Meta:
        model = qpForumTopic
        fields = ["id", "title", "forum", "category", "section"]
        read_only_fields = ["id"]


class qpTopicCreateSerializer(serializers.ModelSerializer):
    """
    Forum Topic serializer
    """

    class Meta:
        model = qpForumTopic
        fields = ["id", "title", "section"]
        read_only_fields = ["id"]


class qpSectionSerializer(serializers.ModelSerializer):
    """
    Forum Section serializer
    """
    category = serializers.SerializerMethodField()
    topics = qpTopicSerializer(many=True)
    breadcrumb = serializers.SerializerMethodField()

    class Meta:
        model = qpForumSection
        fields = ["id", "title", "forum", "category", "topics", "breadcrumb"]
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


class qpSectionCreateSerializer(serializers.ModelSerializer):
    """
    Forum Section serializer
    """
    topics = qpTopicSerializer(many=True)

    class Meta:
        model = qpForumSection
        fields = ["id", "title", "category"]
        read_only_fields = ["id"]


class qpCategorySectionSerializer(serializers.ModelSerializer):
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
                "created_at": last_message.created_at
            }
        return result


class qpCategorySerializer(serializers.ModelSerializer):
    """
    Forum Category serializer
    """
    sections = qpCategorySectionSerializer(many=True)
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


class qpCategoryCreateSerializer(serializers.ModelSerializer):
    """
    Category ``create`` serializer
    """

    class Meta:
        model = qpForumCategory
        fields = ["id", "title", "forum"]
        read_only_fields = ["id", "forum"]


class qpForumSerializer(serializers.ModelSerializer):
    """
    Forum serializer
    """
    owner = serializers.SerializerMethodField()
    categories = qpCategorySerializer(many=True)

    class Meta:
        model = qpForum
        fields = ["id", "owner", "categories"]
        read_only_fields = ["id", "owner", "categories"]
    
    def get_owner(self, obj):
        if obj.rpg.owner:
            return qpUsersSimpleSerializer(obj.rpg.owner.profile).data
        return None


class qpForumCreateSerializer(serializers.ModelSerializer):
    """
    Forum ``create`` serializer
    """

    class Meta:
        model = qpForum
        fields = ["id", "owner"]
        read_only_fields = ["id", "owner"]
