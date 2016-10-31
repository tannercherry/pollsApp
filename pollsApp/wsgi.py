"""
WSGI config for pollsApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pollsApp.settings")

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()


"""from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()"""
