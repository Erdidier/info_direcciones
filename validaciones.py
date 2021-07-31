"""
Creado: Viernes Julio 30 del 2021
@author: Ivan Enrique Couto Campoy y Saúl López Ochoa
Última modificación: Viernes Julio 30 del 2021
"""

import os
from colorama import Fore as color
from colorama import init
import colorama

def limpiar_consola():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def validarIP(ip):
    init(autoreset=True)
    octetos=ip.count(".")
    hexatetos=ip.count(":")
    try:
        if octetos==0 and hexatetos==0:##si no encuentra IPv4 ni IPv6
            print(color.RED+"ERROR: PORFAVOR INGRESA UNA IPv4 o IPv6 VALIDA")
            print(color.RED+"Las IPv4 deben contar con puntos ('.') y 4 octetos")
            print(color.RED+"Las IPv6 deben contar con doble puntos ('.') y 9 hexatetos")
            input(color.YELLOW+"Presionar ENTER para continuar")
            limpiar_consola()
            return False
    
        elif octetos>0 and octetos<3 and hexatetos>0 and hexatetos<7:##si encuentra caracteres de ambos
            print(color.RED+"ERROR: PORFAVOR INGRESA UNA IPv4 o IPv6 VALIDA")
            print(color.RED+"Las IPv4 deben contar con puntos ('.') y 4 octetos")
            print(color.RED+"Las IPv6 deben contar con doble puntos ('.') y 9 hexatetos")
            input(color.YELLOW+"Presionar ENTER para continuar")
            limpiar_consola()
            return False
    
        elif octetos==0 and hexatetos>0 and hexatetos<7:##si encuentra solo IPv6 pero incompleta
            print(color.RED+"ERROR: IPV6 INCOMPLETA")
            print(color.RED+"Una IPv6 debe contar con 8 hexatetos")
            input(color.YELLOW+"Presionar ENTER para continuar")
            limpiar_consola()
            return False
    
        elif octetos>0 and octetos<3 and hexatetos==0:##si encuentra solo IPv4 pero incompleta
            print(color.RED+"ERROR: IPV4 INCOMPLETA")
            print(color.RED+"Una IPv4 debe contar con 4 octetos")
            input(color.YELLOW+"Presionar ENTER para continuar")
            limpiar_consola()
            return False

        if octetos==3 and hexatetos==0:##si encuentra IPv4
            l=ip.split(".")

            for o in l:
                if o.isdigit():##validar que sean todos numeros
                    pass
                else:##si no llegara a ser numero alguno
                    print(color.RED+"ERROR: TODOS LOS VALORES EN LA IPv4 DEBE SER NUMEROS")
                    input(color.YELLOW+"Presionar ENTER para continuar")
                    limpiar_consola()
                    return False

            for o in l:
                o=int(o)
                if o>255:
                    print("ERROR: LOS NUMEROS NO PUEDEN SER MAYORES A 255")
                    input(color.YELLOW+"Presionar ENTER para continuar")
                    limpiar_consola()
                    return False
                else:
                    pass
            print(color.GREEN+"ESTADO IPv4: VALIDA")
            return True


        elif hexatetos==7 and octetos==0:
            hexadecimal=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
            lista=ip.split(":")
            for o in lista:##recorrido por hexateto
                for i in o:#recorrido por caracter
                    if i.upper() in hexadecimal:
                        pass
                    else:
                        print(color.RED+"ERROR: LOS CARACTERES DE LA IPV6 SON:")
                        print(color.RED+"DEL 0 AL 9")
                        print(color.RED+"DE LA 'A' A LA 'F'")
                        input(color.YELLOW+"Presionar ENTER para continuar")
                        limpiar_consola()
                        return False
            print(color.GREEN+"ESTADO IPv6: VALIDA")
            return True

    except:
        print(color.RED+"ERROR NO IDENTIFICADO")
        input(color.YELLOW+"Presionar ENTER para continuar")
        limpiar_consola()
        return False