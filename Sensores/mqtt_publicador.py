from sensores import Concentrador
import sys
import time
import paho.mqtt.client as mqtt
import json


class Publicador:

    def __init__(self):
        self.client = mqtt.Client()
        self.client.connect("34.125.103.25", 1883)
        self.concentrador_1 = Concentrador("invernadero1")
        self.concentrador_2 = Concentrador("invernadero2")

    def publicar_consentrador1(self):
        lista_valores = self.concentrador_1.get_valores()
        temperatura = lista_valores[0]               
        humedad = lista_valores[1]                
        luminosidad = lista_valores[2]
        self.client.publish("SIS/Inv1/temp", json.dumps(temperatura))
        self.client.publish("SIS/Inv1/hume", json.dumps(humedad))
        self.client.publish("SIS/Inv1/lumi", json.dumps(luminosidad))

    def publicar_concentrador2(self):
        lista_valores = self.concentrador_2.get_valores()
        temperatura = lista_valores[0]
        humedad = lista_valores[1]
        luminosidad = lista_valores[2]        
        self.client.publish("SIS/Inv2/temp", json.dumps(temperatura))
        self.client.publish("SIS/Inv2/hume", json.dumps(humedad))
        self.client.publish("SIS/Inv2/lumi", json.dumps(luminosidad))


publicador = Publicador()
while True:
    publicador.publicar_consentrador1()
    print("Enviando datos...")
    # publicador.publicar_concentrador2()
    time.sleep(10)
