from django.urls import path
from knox import views as knox_views

from qp.api.views import (
    qpPingView
)
from qp.api.views.auth import (
    qpRegisterView,
    qpLoginView
)

urlpatterns = [
    path("", qpPingView.as_view()),

    path("register/", qpRegisterView.as_view(), name="auth_register"),
    path("login/", qpLoginView.as_view()),
    path("logout/", knox_views.LogoutAllView.as_view(), name="knox_logoutall")
]