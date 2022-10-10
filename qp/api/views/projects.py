from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_429_TOO_MANY_REQUESTS
from rest_framework.response import Response

from qp.projects.models import qpProject
from qp.api.serializers.projects import qpProjectsCreateSerializer

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
