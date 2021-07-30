"""
Creado: Viernes 30 de Julio del 2021
Author: Saúl López Ochoa
Ultima Modificación: VIernes 30 de Julio del 2021
"""
import requests
from requests import get

class ipstack():

    def __init__(self,ip):
        self.ip=ip##para heredar la variable
    
    def respuesta(self):
        key="fe1df60e18c08b3297e7505efa49cf62"##clave generada en mi cuenta de ipstack
        resp=get("http://api.ipstack.com/"+self.ip+"?access_key="+key).json()#solicitud y transformado a diccionario
        del resp["latitude"],resp["longitude"],resp["location"]##eliminación de datos innecesarios
        return resp##retorno del diccionario
