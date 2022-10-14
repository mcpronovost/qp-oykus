from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Lower
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.status import HTTP_429_TOO_MANY_REQUESTS, HTTP_204_NO_CONTENT
from rest_framework.response import Response

from qp.projects.models import qpProject
from qp.api.serializers.projects import (
    qpProjectsCreateSerializer,
    qpProjectsDetailSerializer,
    qpProjectsDetailOwnerSerializer
)

from qp.notifications.models import qpNotification


class qpProjectsCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = qpProject.objects.all()
    serializer_class = qpProjectsCreateSerializer
    
    def post(self, request, *args, **kwargs):
        max_projects = request.user.profile.limit_max_projects
        count_projects = request.user.owned_projects.filter(is_active=True).count()
        if count_projects >= max_projects:
            return Response({"msg": _("You've reached your limit of owned project (%s).") % (max_projects)}, status=HTTP_429_TOO_MANY_REQUESTS, headers={})
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user, owner=self.request.user)
        try:
            qpNotification.objects.create(
                user_to=self.request.user,
                project_from=qpProject.objects.get(pk=serializer.data["id"]),
                content=str(_("Project « %s » created successfully!") % (str(serializer.data["name"]))),
                has_type="success"
            )
        except Exception as e:
            print('Error on "qpProjectsCreateView" > creating notification : ', e)


class qpProjectsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = qpProject.objects.all()
    serializer_class = qpProjectsDetailSerializer

    def get_queryset(self):
        queryset = super(qpProjectsListView, self).get_queryset()
        queryset = queryset.filter(is_active=True, owner=self.request.user).order_by(Lower("name"))
        return queryset


class qpProjectsDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = qpProject.objects.all()
    serializer_class = qpProjectsDetailSerializer
    lookup_field = "slug"

    def get_object(self, slug):
        try:
            instance = qpProject.objects.get(slug=slug, is_active=True)
            if instance.is_public or (instance.owner == self.request.user):
                return instance
        except Exception as e:
            print("Error on qpProjectsDetailView > get_object : ", e)
        raise Http404

    def get(self, request, slug):
        try:
            instance = self.get_object(slug)
            if instance.owner == self.request.user:
                serializer = qpProjectsDetailOwnerSerializer(instance)
            else:
                serializer = qpProjectsDetailSerializer(instance)
            return Response(serializer.data)
        except Exception as e:
            print("Error on qpProjectsDetailView > get : ", e)
        raise Http404


class qpProjectsDeleteView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = qpProject.objects.all()
    serializer_class = qpProjectsDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super(qpProjectsDeleteView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_update(self, serializer):
        serializer.save(is_active=False)

    def patch(self, request, *args, **kwargs):
        self.partial_update(request, *args, **kwargs)
        return Response(status=HTTP_204_NO_CONTENT)
