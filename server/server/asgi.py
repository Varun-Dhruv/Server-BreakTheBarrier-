"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""


from django.urls import path, include
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from SignLanguageDetection.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

ws_patterns=[
    path('ws/test', TestConsumer.as_asgi())
]

application=ProtocolTypeRouter({
    'websocket':URLRouter(ws_patterns),    
    'http': get_asgi_application(),
})
