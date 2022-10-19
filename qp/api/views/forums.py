from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from qp.api.permissions import qpIsAuthenticated
from qp.forums.models import *
from qp.api.serializers.forums import *


class qpForumsView(ListAPIView):
    """
    ``GET LIST``: qpForum
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForum.objects.all()
    serializer_class = qpForumSerializer


class qpForumsCreateView(CreateAPIView):
    """
    ``POST CREATE``: qpForum
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForum.objects.all()
    serializer_class = qpForumCreateSerializer

    def post(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``CREATE`` """
        # ex: is user reached his max forums created
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """ Add current user as owner on ``CREATE`` """
        serializer.save(owner=self.request.user)


class qpForumsDetailView(RetrieveUpdateAPIView):
    """
    ``GET``,``UPDATE``: qpForum
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForum.objects.all()
    serializer_class = qpForumSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner == self.request.user:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpForumsCategoriesListView(ListAPIView):
    """
    ``GET LIST``: qpForum > qpCategory
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpCategorySerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumCategory.objects.filter(forum__id=pk)
        except Exception as e:
            print("Error on ``qpForumsCategoriesListView`` > get_queryset : ", e)
            return qpForumCategory.objects.none()
        return queryset


class qpForumsSectionsListView(ListAPIView):
    """
    ``GET LIST``: qpForum > qpSection
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpSectionSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumSection.objects.filter(forum__id=pk)
        except Exception as e:
            print("Error on ``qpForumsSectionsListView`` > get_queryset : ", e)
            return qpForumSection.objects.none()
        return queryset


class qpForumsTopicsListView(ListAPIView):
    """
    ``GET LIST``: qpForum > qpTopic.
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpTopicSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumTopic.objects.filter(forum__id=pk)
        except Exception as e:
            print("Error on ``qpForumsTopicsListView`` > get_queryset : ", e)
            return qpForumTopic.objects.none()
        return queryset


class qpForumsMessagesListView(ListAPIView):
    """
    ``GET LIST``: qpForum > qpMessage
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpMessageSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumMessage.objects.filter(forum__id=pk)
        except Exception as e:
            print("Error on ``qpForumsMessagesListView`` > get_queryset : ", e)
            return qpForumMessage.objects.none()
        return queryset


class qpForumsCategoriesView(ListAPIView):
    """
    ``GET LIST``: qpForumCategory
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumCategory.objects.all()
    serializer_class = qpCategorySerializer


class qpForumsCategoriesCreateView(CreateAPIView):
    """
    ``POST CREATE``: qpForumCategory
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumCategory.objects.all()
    serializer_class = qpCategoryCreateSerializer

    def post(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``CREATE`` """
        # ex: is forum accept create from this user
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """ Add automatically retrieved data on ``CREATE`` """
        serializer.save()


class qpForumsCategoriesDetailView(RetrieveUpdateAPIView):
    """
    ``GET``,``UPDATE``: qpForumCategory
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumCategory.objects.all()
    serializer_class = qpCategorySerializer

    def patch(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``UPDATE`` """
        can_update = False
        # instance = self.get_object()
        # if instance.owner == self.request.user:
        #    can_patch = True
        if can_update:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpForumsCategoriesSectionsView(ListAPIView):
    """
    ``GET LIST``: qpForumCategory > qpSection
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpSectionSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumSection.objects.filter(category__id=pk)
        except Exception as e:
            print("Error on ``qpForumsCategoriesSectionsView`` > get_queryset : ", e)
            return qpForumSection.objects.none()
        return queryset


class qpForumsCategoriesTopicsView(ListAPIView):
    """
    ``GET LIST``: qpForumCategory > qpTopic.
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpTopicSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumTopic.objects.filter(category__id=pk)
        except Exception as e:
            print("Error on ``qpForumsCategoriesTopicsView`` > get_queryset : ", e)
            return qpForumTopic.objects.none()
        return queryset


class qpForumsCategoriesMessagesView(ListAPIView):
    """
    ``GET LIST``: qpForumCategory > qpMessage
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpMessageSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumMessage.objects.filter(category__id=pk)
        except Exception as e:
            print("Error on ``qpForumsCategoriesMessagesView`` > get_queryset : ", e)
            return qpForumMessage.objects.none()
        return queryset


class qpForumsSectionsView(ListAPIView):
    """
    ``GET LIST``: qpForumsSection
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumSection.objects.all()
    serializer_class = qpSectionSerializer


class qpForumsSectionsCreateView(CreateAPIView):
    """
    ``POST CREATE``: qpForumsSection
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumSection.objects.all()
    serializer_class = qpSectionCreateSerializer

    def post(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``CREATE`` """
        # ex: is forum accept create from this user
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """ Add automatically retrieved data on ``CREATE`` """
        serializer.save()


class qpForumsSectionsDetailView(RetrieveUpdateAPIView):
    """
    ``GET``,``UPDATE``: qpForumsSection
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumSection.objects.all()
    serializer_class = qpSectionSerializer

    def patch(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``UPDATE`` """
        can_update = False
        # instance = self.get_object()
        # if instance.owner == self.request.user:
        #    can_patch = True
        if can_update:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpForumsSectionsTopicsView(ListAPIView):
    """
    ``GET LIST``: qpForumsSection > qpTopic.
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpTopicSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumTopic.objects.filter(category__id=pk)
        except Exception as e:
            print("Error on ``qpForumsSectionsTopicsView`` > get_queryset : ", e)
            return qpForumTopic.objects.none()
        return queryset


class qpForumsSectionsMessagesView(ListAPIView):
    """
    ``GET LIST``: qpForumsSection > qpMessage
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpMessageSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumMessage.objects.filter(category__id=pk)
        except Exception as e:
            print("Error on ``qpForumsSectionsMessagesView`` > get_queryset : ", e)
            return qpForumMessage.objects.none()
        return queryset


class qpForumsTopicsView(ListAPIView):
    """
    ``GET LIST``: qpForumsTopic
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumTopic.objects.all()
    serializer_class = qpTopicSerializer


class qpForumsTopicsCreateView(CreateAPIView):
    """
    ``POST CREATE``: qpForumsTopic
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumTopic.objects.all()
    serializer_class = qpTopicCreateSerializer

    def post(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``CREATE`` """
        # ex: is forum accept create from this user
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """ Add automatically retrieved data on ``CREATE`` """
        serializer.save()


class qpForumsTopicsDetailView(RetrieveUpdateAPIView):
    """
    ``GET``,``UPDATE``: qpForumsTopic
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumTopic.objects.all()
    serializer_class = qpTopicSerializer

    def patch(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``UPDATE`` """
        can_update = False
        # instance = self.get_object()
        # if instance.owner == self.request.user:
        #    can_patch = True
        if can_update:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class qpForumsTopicsMessagesView(ListAPIView):
    """
    ``GET LIST``: qpForumsTopic > qpMessage
    """
    permission_classes = [qpIsAuthenticated]
    serializer_class = qpMessageSerializer

    def get_queryset(self):
        try:
            pk = int(self.kwargs["pk"])
            queryset = qpForumMessage.objects.filter(category__id=pk)
        except Exception as e:
            print("Error on ``qpForumsTopicsMessagesView`` > get_queryset : ", e)
            return qpForumMessage.objects.none()
        return queryset


class qpForumsMessagesView(ListAPIView):
    """
    ``GET LIST``: qpForumMessage
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumMessage.objects.all()
    serializer_class = qpMessageSerializer


class qpForumsMessagesCreateView(CreateAPIView):
    """
    ``POST CREATE``: qpForumMessage
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumMessage.objects.all()
    serializer_class = qpMessageCreateSerializer

    def post(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``CREATE`` """
        # ex: is forum accept create from this user
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        # return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        """ Add automatically retrieved data on ``CREATE`` """
        serializer.save()


class qpForumsMessagesDetailView(RetrieveUpdateAPIView):
    """
    ``GET``,``UPDATE``: qpForumMessage
    """
    permission_classes = [qpIsAuthenticated]
    queryset = qpForumMessage.objects.all()
    serializer_class = qpMessageSerializer

    def patch(self, request, *args, **kwargs):
        """ Verify if user have authorization before ``UPDATE`` """
        can_update = False
        # instance = self.get_object()
        # if instance.owner == self.request.user:
        #    can_patch = True
        if can_update:
            return self.partial_update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
