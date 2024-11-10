import json
from channels.generic.websocket import AsyncWebsocketConsumer

class IntruderActionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("intruder_notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("intruder_notifications", self.channel_name)

    async def notify_intruder_action(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event["message"]))
