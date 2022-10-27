from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ForumsConfig(AppConfig):
    name = "qp.forums"
    verbose_name = _("Forums")