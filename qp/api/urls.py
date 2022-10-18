from django.urls import path
from knox import views as knox_views

from qp.api.views import qpPingView
from qp.api.views.auth import *
from qp.api.views.me import *
from qp.api.views.forums import *

"""
/api/v1/forums/

/api/v1/forums/<int:pk>/
/api/v1/forums/<int:pk>/categories/
/api/v1/forums/<int:pk>/sections/
/api/v1/forums/<int:pk>/topics/

/api/v1/forums/categories/<int:pk>/
/api/v1/forums/categories/<int:pk>/sections/
/api/v1/forums/categories/<int:pk>/topics/

/api/v1/forums/sections/<int:pk>/
/api/v1/forums/sections/<int:pk>/topics/

/api/v1/forums/topics/<int:pk>/
/api/v1/forums/topics/<int:pk>/messages/

/api/v1/forums/messages/<int:pk>/


/api/v1/projects/                       (create, getlist)               qpProjectsView
/api/v1/projects/<slug>/                (get, patch, delete)            qpProjectsDetailView
/api/v1/projects/<slug>/tasks/          (create, getlist)               qpProjectsTasksView
/api/v1/projects/<slug>/tasks/<id>/     (get, patch, delete)            qpProjectsTasksDetailView


/api/v1/tasks/                          (create, getlist)               qpTasksView
/api/v1/tasks/<id>/                     (get, patch, delete)            qpTasksDetailView


/api/v1/notifications/                  (getlist, patchlist)            qpNotificationsView
/api/v1/notifications/<id>/             (get, patch, delete)            qpNotificationsDetailView
"""

urlpatterns = [
    path("", qpPingView.as_view()),
    path("me/", qpMeView.as_view()),

    path("forums/", qpForumsView.as_view()),
    path("forums/create/", qpForumsCreateView.as_view()),
    path("forums/<int:pk>/", qpForumsDetailView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logout-all/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),

    path("<path:fallback>", qpPingView.as_view())
]