from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Makemessages without venv."

    def handle(self, *args, **options):
        call_command("makemessages", "--locale", "fr", "-i", "venv")
        call_command("makemessages", "--locale", "en", "-i", "venv")