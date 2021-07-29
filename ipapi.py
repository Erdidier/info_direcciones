"""
Creado: Sábado Julio 17 20:04 2021
@author: Erick Didier Hernández Victoriano
Última modificación: Jueves Julio 29 12:23 2021
"""

from requests import get

def ipapi():
    ip = input("Ingrese la dirección IP pública que desea analizar: ")

    loc = get('https://ipapi.co/'+ip+'/json/')
    dic_ip = loc.json()
    return dic_ip

print(ipapi())
