"""
Creado: Viernes Julio 30 04:25 2021
@author: Jazmin Guadalupe Salgado Arrollo
Última modificación: Viernes Julio 30 2021
"""

import ipapi
import Apistack

class info_dir:
        
    while True:
        opc = input("Elige la api a utilizar:\na)ipstack\nb)ipapi\nc)salir\n")
        opc = opc.lower()
        if opc == "a":
            ip = input("Ingrese la dirección IP pública que desea analizar: ")
            ipstack = Apistack.ipstack(ip)
            info = ipstack.respuesta()
            print(info)
        if opc == "b":
            ip = input("Ingrese la dirección IP pública que desea analizar: ")
            info = ipapi.ipapi(ip)
            print(info)
        if opc == "c":
            break
        else:
            print("Favor de ingresar una opción dentro de la lista anterior")

app = info_dir


