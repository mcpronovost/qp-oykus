from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CharactersConfig(AppConfig):
    name = "qp.characters"
    verbose_name = _("Characters")