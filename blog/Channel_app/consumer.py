from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event): # conn establishment
        print("Client connected")
        self.send({
            "type": "websocket.accept",
            "message":"Welcome to the chat!!"
        })

    def websocket_receive(self, event): # handles comm b/w client and server
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    def websocket_disconnect(self, event): # handles disconnection
        pass


class MyConsumer(WebsocketConsumer):
    connected_clients = [] # list to store connected clients to the server

    def connect(self): # conn request
        self.accept() # accept the conn request
        self.connected_clients.append(self) # Myconsumer instance is added to the list

        # print(self.scope)
        print("client", self.scope['client'])
        self.send(text_data='Welcome, You are connected!!')

    def receive(self, text_data): 
        message=text_data

        for client in self.connected_clients: # broadcast to all connected clients
            client.send(text_data=json.dumps({
                'from':str(self.scope['client']),
                'message':message
            }))

    def disconnect(self, close_code):
        if self in self.connected_clients:
            self.connected_clients.remove(self)
        
        print("Client disconnected",self.scope['client']) # remove the client from the list when disconnected