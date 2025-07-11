from django.urls import path
from . import consumer

ws_urlpatterns = [
    path('ws/chat/',consumer.MyConsumer.as_asgi())
]