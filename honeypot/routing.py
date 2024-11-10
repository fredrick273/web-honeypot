from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/intruder/', consumers.IntruderActionConsumer.as_asgi()),
]
