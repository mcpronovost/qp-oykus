from django.utils.translation import gettext_lazy as _
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAny, qpIsAuthenticated
from qp.rpg.models import qpRpg
from qp.forums.models import qpForum, qpForumCategory, qpForumSection, qpForumTopic, qpForumMessage
from qp.api.serializers.forums import qpForumSerializer
from qp.api.serializers.forums.categories import qpForumCategorySerializer
from qp.api.serializers.forums.sections import qpForumSectionSerializer
from qp.api.serializers.forums.topics import qpForumTopicSerializer
from qp.api.serializers.forums.messages import qpForumMessageSerializer


class qpForumsDetailView(RetrieveUpdateAPIView):
    """
    Forums `GET`, `UPDATE`, `DELETE`
    """
    permission_classes = [qpIsAny]
    queryset = qpForum.objects.all()
    serializer_class = qpForumSerializer

    def get_object(self):
        rpg = qpRpg.objects.filter(slug=self.kwargs["slug"]).first()
        if rpg is None:
            raise Http404
        obj = rpg.forum
        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class qpForumCategoriesDetailView(RetrieveUpdateAPIView):
    """
    ForumCategories `GET`, `UPDATE`, `DELETE`
    """
    permission_classes = [qpIsAny]
    queryset = qpForumCategory.objects.all()
    serializer_class = qpForumCategorySerializer

    def get_object(self):
        slug = self.kwargs["slug"]
        pk = self.kwargs["pk"]
        rpg = qpRpg.objects.filter(slug=slug).first()
        if rpg is None:
            raise Http404
        obj = rpg.forum.categories.filter(pk=pk).first()
        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class qpForumSectionsDetailView(RetrieveUpdateAPIView):
    """
    ForumSections `GET`, `UPDATE`, `DELETE`
    """
    permission_classes = [qpIsAny]
    queryset = qpForumSection.objects.all()
    serializer_class = qpForumSectionSerializer

    def get_object(self):
        slug = self.kwargs["slug"]
        pk = self.kwargs["pk"]
        rpg = qpRpg.objects.filter(slug=slug).first()
        if rpg is None:
            raise Http404
        obj = rpg.forum.sections.filter(pk=pk).first()
        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class qpForumTopicsDetailView(RetrieveUpdateAPIView):
    """
    ForumTopics `GET`, `UPDATE`, `DELETE`
    """
    permission_classes = [qpIsAny]
    queryset = qpForumTopic.objects.all()
    serializer_class = qpForumTopicSerializer

    def get_object(self):
        slug = self.kwargs["slug"]
        pk = self.kwargs["pk"]
        rpg = qpRpg.objects.filter(slug=slug).first()
        if rpg is None:
            raise Http404
        obj = rpg.forum.topics.filter(pk=pk).first()
        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if user is not None and user.is_authenticated and user.profile and instance.owner == user:
            return self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class qpForumTopicMessagesListView(ListAPIView):
    """
    ForumTopicMessages `GET` list
    """
    permission_classes = [qpIsAny]
    queryset = qpForumMessage.objects.all()
    serializer_class = qpForumMessageSerializer
    page_size = 6

    def get_object(self):
        slug = self.kwargs["slug"]
        pk = self.kwargs["pk"]
        rpg = qpRpg.objects.filter(slug=slug).first()
        if rpg is None:
            raise Http404
        obj = rpg.forum.topics.filter(pk=pk).first()
        if obj is None:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        topic = self.get_object()
        queryset = topic.messages.all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
