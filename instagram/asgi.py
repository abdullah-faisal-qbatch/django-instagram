"""
ASGI config for instagram project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# from channels.security.websocket import AllowedHostsOriginValidator
# import chat.routing
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import os
# from django.core.asgi import get_asgi_application
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "instagram.settings")

# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')

# django_asgi_app = get_asgi_application()

# # django_asgi_app = ProtocolTypeRouter({
# #     "http": application
# # })


# # Initialize Django ASGI application early to ensure the AppRegistry
# # # is populated before importing code that may import ORM models. django_asgi_app = get_asgi_application()
# application = ProtocolTypeRouter({"http": django_asgi_app,
#                                   "websocket": AllowedHostsOriginValidator(
#                                       AuthMiddlewareStack(
#                                           URLRouter(
#                                               chat.routing.websocket_urlpatterns)))})


# from channels.routing import ProtocolTypeRouter, URLRouter
# from chat import routing
# from channels.auth import AuthMiddlewareStack
# import os
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')


# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(
#                 routing.websocket_urlpatterns
#             )
#         )
#     }
# )


import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})
