"""
Creado: Viernes Julio 30 04:25 2021
@author: Jazmin Guadalupe Salgado Arrollo
Última modificación: Viernes Julio 30 2021
"""
from ipapi import *
from Apistack import *
from colorama import Fore as color
from colorama import init
import colorama
from validaciones import *
from tabulate import *





class info_dir:
    init(autoreset=True)##para que se visualice en CLI de linux y windows    
        
    while True:

        opc = input(color.WHITE+"Elige la api a utilizar:\na)ipstack\nb)ipapi\nc)salir\n")
        opc = opc.lower()
        if opc == "a":
            print(color.BLUE+"PAGINA PARA CONSULTAR TU IP - https://www.whatismyip.com/my-ip-information/")
            ip = input("Ingrese la dirección IP pública que desea analizar: ")
            verificar=validarIP(ip)
            if verificar==True:
                Apistack=ipstack(ip)
                info=Apistack.respuesta()
                lista=[]
                i=int(1)
                for dato in info.items():
                    if dato[1]== None and i!=2:
                        lista.append([color.RED+dato[0],color.BLUE+"N/A"])
                    elif dato[1]== None and i==2:
                        print(color.RED+"ERROR")
                        print(color.YELLOW+"Posiblemente ingresaste una IP privada")
                        print(color.YELLOW+"Te dejamos un link donde consultar tus IPs Publicas")
                        print(color.BLUE+"https://www.whatismyip.com/es/")
                        input(color.YELLOW+"Presiona ENTER para continuar")
                        limpiar_consola()
                        lista=[]
                        break
                    else:
                        lista.append([color.RED+dato[0],color.BLUE+dato[1]])
                    i=i+1
                if len(lista)>0:
                    print(tabulate(lista, tablefmt="simple"))
                    input(color.YELLOW+"Presiona ENTER para continuar")
                    limpiar_consola()
                else:
                    pass

        elif opc == "b":
            print(color.BLUE+"PAGINA PARA CONSULTAR TU IP - https://www.whatismyip.com/my-ip-information/")
            ip = input("Ingrese la dirección IP pública que desea analizar: ")
            verificar=validarIP(ip)
            if verificar==True:
                info=ipapi(ip)
                lista=[]
                i=int(1)
                for dato in info.items():
                    if dato[1]=="Reserved IP Address":
                        print(color.RED+"Error IPv4 privada")
                        print(color.YELLOW+"Te dejamos un link donde consultar tus IPs Publicas")
                        print(color.BLUE+"https://www.whatismyip.com/es/")
                        input(color.YELLOW+"Presiona ENTER para continuar")
                        limpiar_consola()
                        lista=[]
                        break
                    elif dato[1]==None:
                        lista.append([color.RED+dato[0],color.BLUE+"N/A"])
                    elif dato[1]=="Invalid IP Address":
                        print(color.RED+"ERROR: VERIFICA QUE TU IP ESTE BIEN ESCRITA")
                        print(color.YELLOW+"Te dejamos un link donde consultar tus IPs Publicas")
                        print(color.BLUE+"https://www.whatismyip.com/es/")
                        input(color.YELLOW+"Presiona ENTER para continuar")
                    elif type(dato[1])==bool:
                        pass
                    elif type(dato[1])==float:
                        lista.append([color.RED+dato[0],color.BLUE+str(dato[1])])
                    else:
                        lista.append([color.RED+dato[0],color.BLUE+dato[1]])
                    i=i+1
                print(tabulate(lista, tablefmt="simple"))
                input(color.YELLOW+"Presiona ENTER para continuar")
                limpiar_consola()
        elif opc == "c":
            break
        else:
            print("Favor de ingresar una opción dentro de la lista anterior")

