import os
import django

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

django.setup()

from chat.routing import websocket_urlpatterns

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hillspay.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
	{
		'http': django_asgi_app,
		'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlpatterns))),
	}
)
