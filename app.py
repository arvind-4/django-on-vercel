"""Entry point for the WSGI server to serve the Django application."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = get_wsgi_application()
