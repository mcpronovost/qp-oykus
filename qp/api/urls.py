from django.urls import path
from knox import views as knox_views

from qp.api.views import qpPingView
from qp.api.views.auth import qpRegisterView, qpLoginView
from qp.api.views.me import qpMeView
from qp.api.views.notifications import qpNotificationsSeenView, qpNotificationsAllSeenView
from qp.api.views.projects import (
    qpProjectsCreateView,
    qpProjectsDetailView
)

urlpatterns = [
    path("", qpPingView.as_view()),
    path("me/", qpMeView.as_view()),

    path("notifications/seen/", qpNotificationsAllSeenView.as_view()),
    path("notifications/<int:pk>/seen/", qpNotificationsSeenView.as_view()),

    path("projects/create/", qpProjectsCreateView.as_view()),
    path("projects/<slug:slug>/", qpProjectsDetailView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("logout-all/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),

    path("<path:fallback>", qpPingView.as_view())
]