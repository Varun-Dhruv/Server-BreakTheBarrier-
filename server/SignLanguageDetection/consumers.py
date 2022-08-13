from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"

        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name)
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected'}))
        # Called on connection.
        # To accept the connection call:
        # self.accept()
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # self.accept("subprotocol")
        # To reject the connection, call:
        # self.close()

    def receive(self, text_data):
        print(text_data)
        pass
        

    def disonnect(self):
        print("Disconnected")
        
