"""
Creado: Sábado Julio 17 20:04 2021
@author: Erick Didier Hernández Victoriano
Última modificación: Jueves Julio 29 12:23 2021
"""

from requests import get

def ipapi(ip):
    loc = get('https://ipapi.co/'+ip+'/json/')
    dic_ip = loc.json()
    try:
        del dic_ip["country_code_iso3"],dic_ip["country_capital"]
        del dic_ip["country_tld"],dic_ip["continent_code"],dic_ip["in_eu"]
        del dic_ip["latitude"],dic_ip["longitude"],dic_ip["timezone"]
        del dic_ip["utc_offset"],dic_ip["country_calling_code"]
        del dic_ip["currency"],dic_ip["currency_name"],dic_ip["languages"]
        del dic_ip["country_area"],dic_ip["country_population"]
        del dic_ip["asn"],dic_ip["org"]
        return dic_ip
    except:
        return dic_ip

#print(ipapi(ip))