import random
import json


class Sensor:

    def __init__(self, nombre, tipo_medida, rango: tuple):
        self.nombre = nombre
        self.tipo_medida = tipo_medida
        self.rango = rango


    def get_valor(self):
        valor = random.randint(self.rango[0], self.rango[1])
        info = {"dato": self.nombre, "valor": valor}
        return info


class Concentrador:

    def __init__(self, nombre_invernadero: str):
        self.sensor_temperatura = Sensor("Temperatura", "Grados", (20, 40))
        self.sensor_humedad = Sensor("Humedad", "Medida", (10, 30))
        self.sensor_luminosidad = Sensor("Luminosidad", "Candelas", (0, 10))
        self.nombre_invernadero = nombre_invernadero

    def get_valores(self):
        temperatura = self.sensor_temperatura.get_valor()
        # temperatura['nombre_invernadero'] = self.nombre_invernadero

        humedad = self.sensor_humedad.get_valor()
        # humedad['nombre_invernadero'] = self.nombre_invernadero

        luminocidad = self.sensor_luminosidad.get_valor()
        # luminocidad['nombre_invernadero'] = self.nombre_invernadero


        lista_valores = [temperatura, humedad, luminocidad]
        return lista_valores
