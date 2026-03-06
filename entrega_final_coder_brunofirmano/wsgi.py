"""
WSGI config for entrega_final_coder_brunofirmano project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'entrega_final_coder_brunofirmano.settings')

application = get_wsgi_application()
