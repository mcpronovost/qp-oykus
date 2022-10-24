from django.urls import path
from knox import views as knox_views

from qp.api.views.auth import *
from qp.api.views.me import *
from qp.api.views.rpg import *
from qp.api.views.forums import *

"""
/api/v1/forums/

/api/v1/forums/<int:pk>/
/api/v1/forums/<int:pk>/categories/
/api/v1/forums/<int:pk>/sections/
/api/v1/forums/<int:pk>/topics/
/api/v1/forums/<int:pk>/messages/

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

    path("rpg/", qpRpgListView.as_view()),
    path("rpg/create/", qpRpgCreateView.as_view()),
    path("rpg/<slug:slug>/", qpRpgDetailView.as_view()),

    path("forums/", qpForumsView.as_view()),
    path("forums/create/", qpForumsCreateView.as_view()),
    path("forums/<int:pk>/", qpForumsDetailView.as_view()),
    path("forums/<int:pk>/categories/", qpForumsCategoriesListView.as_view()),
    path("forums/<int:pk>/sections/", qpForumsSectionsListView.as_view()),
    path("forums/<int:pk>/topics/", qpForumsTopicsListView.as_view()),
    path("forums/<int:pk>/messages/", qpForumsMessagesListView.as_view()),
    path("forums/categories/", qpForumsCategoriesView.as_view()),
    path("forums/categories/create/", qpForumsCategoriesCreateView.as_view()),
    path("forums/categories/<int:pk>/", qpForumsCategoriesDetailView.as_view()),
    path("forums/categories/<int:pk>/sections/", qpForumsCategoriesSectionsView.as_view()),
    path("forums/categories/<int:pk>/topics/", qpForumsCategoriesTopicsView.as_view()),
    path("forums/categories/<int:pk>/messages/", qpForumsCategoriesMessagesView.as_view()),
    path("forums/sections/", qpForumsSectionsView.as_view()),
    path("forums/sections/create/", qpForumsSectionsCreateView.as_view()),
    path("forums/sections/<int:pk>/", qpForumsSectionsDetailView.as_view()),
    path("forums/sections/<int:pk>/topics/", qpForumsSectionsTopicsView.as_view()),
    path("forums/sections/<int:pk>/messages/", qpForumsSectionsMessagesView.as_view()),
    path("forums/topics/", qpForumsTopicsView.as_view()),
    path("forums/topics/create/", qpForumsTopicsCreateView.as_view()),
    path("forums/topics/<int:pk>/", qpForumsTopicsDetailView.as_view()),
    path("forums/topics/<int:pk>/messages/", qpForumsTopicsMessagesView.as_view()),
    path("forums/messages/", qpForumsMessagesView.as_view()),
    path("forums/messages/create/", qpForumsMessagesCreateView.as_view()),
    path("forums/messages/<int:pk>/", qpForumsMessagesDetailView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logout-all/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),

    #path("<path:fallback>", qpPingView.as_view())
]