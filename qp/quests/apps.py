from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class QuestsConfig(AppConfig):
    name = "qp.quests"
    verbose_name = _("Quests")