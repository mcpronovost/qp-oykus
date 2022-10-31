from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from qp.api.serializers.users import qpUsersSimpleSerializer
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
    topics = qpTopicSerializer(many=True)

    class Meta:
        model = qpForumSection
        fields = ["id", "title", "forum", "category", "topics"]
        read_only_fields = ["id"]


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

    class Meta:
        model = qpForumSection
        fields = ["id", "title", "forum", "category"]
        read_only_fields = ["id"]


class qpCategorySerializer(serializers.ModelSerializer):
    """
    Forum Category serializer
    """
    sections = qpCategorySectionSerializer(many=True)

    class Meta:
        model = qpForumCategory
        fields = ["id", "title", "forum", "sections"]
        read_only_fields = ["id"]


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
        if obj.owner:
            return qpUsersSimpleSerializer(obj.owner.profile).data
        return None


class qpForumCreateSerializer(serializers.ModelSerializer):
    """
    Forum ``create`` serializer
    """

    class Meta:
        model = qpForum
        fields = ["id", "owner"]
        read_only_fields = ["id", "owner"]
