from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path
from qp.settings import MEDIA_ROOT, MEDIA_URL

from qp.views import app

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api-auth/", include("rest_framework.urls")),
    re_path(r"^api/auth/", include("knox.urls")),
    re_path(r"^api/", include("qp.api.urls")),

    re_path(r"^", app)
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
