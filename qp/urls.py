from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from qp.settings import STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

from qp.views import app, api_v1, test

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api-auth/", include("rest_framework.urls")),
    re_path(r"^api/auth/", include("knox.urls")),
    re_path(r"^api/$", api_v1),
    re_path(r"^api/v1/", include("qp.api.urls")),
    re_path(r"^test/$", test),
] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT) + [
    re_path(r"^", app)
]
