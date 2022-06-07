import paho.mqtt.client as mqtt
import json


class Cliente:

    def __init__(self, nombre_invernadero):
        self.nombre_invernadero = nombre_invernadero
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

    def on_message(self, client, userdata, msg):  
        mensaje = msg.payload
        data = json.loads(mensaje)   
        print(data)

    def on_connect(self, client, userdata, flags, rc):
        print("Se conecto con mqtt" + str(rc))
        topic = "SIS/Act"
        self.client.subscribe(topic)

    def conectar(self):
        self.client.connect("34.125.103.25", 1883)
        self.client.loop_forever()

cliente = Cliente("Inv1")
cliente.conectar()
