"""
WSGI config for knut_sugang project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('C:/Apache24/htdocs/knut-sugang')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knut_sugang.settings')

application = get_wsgi_application()
