"""
WSGI config for ft_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
    
from django.core.wsgi import get_wsgi_application
    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ft_api.settings")
    
config = os.environ.get('DJANGO_CONFIGURATION')
if not config:
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')
    
from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()
