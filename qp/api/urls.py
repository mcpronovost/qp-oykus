from django.urls import path
from knox import views as knox_views

from qp.api.views.auth import *
from qp.api.views.me import *
from qp.api.views.rpg import *
from qp.api.views.characters import *
from qp.api.views.races import *
from qp.api.views.skills import *
from qp.api.views.forums import *

urlpatterns = [
    path("", qpPingView.as_view()),
    path("me/", qpMeView.as_view()),
    path("me/rpg/", qpMeRpgListView.as_view()),
    path("me/characters/", qpMeCharactersListView.as_view()),

    path("rpg/", qpRpgListView.as_view()),
    path("rpg/create/", qpRpgCreateView.as_view()),
    path("rpg/<slug:slug>/", qpRpgDetailView.as_view()),
    path("rpg/<slug:slug>/delete/", qpRpgDeleteView.as_view()),
    path("rpg/<slug:slug>/races/", qpRpgRacesListView.as_view()),
    path("rpg/<slug:slug>/skills/", qpRpgSkillsListView.as_view()),
    path("rpg/<slug:slug>/characters/", qpRpgCharactersListView.as_view()),

    path("characters/", qpCharactersListView.as_view()),
    path("characters/create/", qpCharactersCreateView.as_view()),
    path("characters/<int:pk>/", qpCharactersDetailView.as_view()),
    path("characters/<int:pk>/delete/", qpCharactersDeleteView.as_view()),

    path("races/", qpRacesListView.as_view()),
    path("races/create/", qpRacesCreateView.as_view()),
    path("races/<int:pk>/", qpRacesDetailView.as_view()),
    path("races/<int:pk>/delete/", qpRacesDeleteView.as_view()),

    path("skills/", qpSkillsListView.as_view()),
    path("skills/create/", qpSkillsCreateView.as_view()),
    path("skills/<int:pk>/", qpSkillsDetailView.as_view()),
    path("skills/<int:pk>/delete/", qpSkillsDeleteView.as_view()),

    path("forums/", qpForumsListView.as_view()),
    path("forums/create/", qpForumsCreateView.as_view()),
    path("forums/<int:pk>/", qpForumsDetailView.as_view()),
    path("forums/<int:pk>/categories/", qpForumsCategoriesListView.as_view()),
    path("forums/<int:pk>/sections/", qpForumsSectionsListView.as_view()),
    path("forums/<int:pk>/topics/", qpForumsTopicsListView.as_view()),
    path("forums/<int:pk>/messages/", qpForumsMessagesListView.as_view()),
    path("forums/categories/", qpCategoriesListView.as_view()),
    path("forums/categories/create/", qpCategoriesCreateView.as_view()),
    path("forums/categories/<int:pk>/", qpCategoriesDetailView.as_view()),
    path("forums/categories/<int:pk>/sections/", qpCategoriesSectionsListView.as_view()),
    path("forums/categories/<int:pk>/topics/", qpCategoriesTopicsListView.as_view()),
    path("forums/categories/<int:pk>/messages/", qpCategoriesMessagesListView.as_view()),
    path("forums/sections/", qpSectionsListView.as_view()),
    path("forums/sections/create/", qpSectionsCreateView.as_view()),
    path("forums/sections/<int:pk>/", qpSectionsDetailView.as_view()),
    path("forums/sections/<int:pk>/topics/", qpSectionsTopicsListView.as_view()),
    path("forums/sections/<int:pk>/messages/", qpSectionsMessagesListView.as_view()),
    path("forums/topics/", qpTopicsListView.as_view()),
    path("forums/topics/create/", qpTopicsCreateView.as_view()),
    path("forums/topics/<int:pk>/", qpTopicsDetailView.as_view()),
    path("forums/topics/<int:pk>/messages/", qpTopicsMessagesListView.as_view()),
    path("forums/messages/", qpMessagesListView.as_view()),
    path("forums/messages/create/", qpMessagesCreateView.as_view()),
    path("forums/messages/<int:pk>/", qpMessagesDetailView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logout-all/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),

    #path("<path:fallback>", qpPingView.as_view())
]