from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Compilemessages without venv."

    def handle(self, *args, **options):
        call_command("compilemessages", "--ignore=cache", "--ignore=venv/*")