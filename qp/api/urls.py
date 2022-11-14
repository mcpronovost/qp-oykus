from django.urls import path
from knox import views as knox_views

from qp.api.views import qpPingView
from qp.api.views.auth import qpLoginView, qpRegisterView
from qp.api.views.me import qpMeView
from qp.api.views.rpg import qpRpgListView, qpRpgDetailView

urlpatterns = [
    path("", qpPingView.as_view()),
    path("me/", qpMeView.as_view()),

    # path("users/", qpPingView.as_view()),
    # path("users/<int:pk>/", qpPingView.as_view()),

    path("rpg/", qpRpgListView.as_view()),
    path("rpg/<slug:slug>/", qpRpgDetailView.as_view()),

    # path("rpg/<slug:slug>/races/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/races/<int:pk>/", qpPingView.as_view()),

    # path("rpg/<slug:slug>/skills/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/skills/<int:pk>/", qpPingView.as_view()),

    # path("rpg/<slug:slug>/forum/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/categories/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/categories/<int:pk>/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/sections/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/sections/<int:pk>/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/topics/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/topics/<int:pk>/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/messages/", qpPingView.as_view()),
    # path("rpg/<slug:slug>/forum/messages/<int:pk>/", qpPingView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logout-all/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]