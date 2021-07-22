"""
Creado: Sábado Julio 17 20:04 2021
@author: Erick Didier Hernández Victoriano
Última modificación: Miércoles Julio 21 19:14 2021
"""

from requests import get

ip = input("Ingrese la dirección IP pública que desea analizar: ")

loc = get('https://ipapi.co/'+ip+'/json/')
dic_ip = loc.json()
print (dic_ip)
