from ncclient import manager
import xml.dom.minidom
from click import command
from webex_bot.models.command import Command
import json
import requests
requests.packages.urllib3.disable_warnings()

direccion_equipo = "192.168.0.23"
credenciales = ["cisco","cisco123!"]

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
}
basicauth = (credenciales[0], credenciales[1])

############################MENU############################

class Menu(Command):
    def __init__(self):
        super().__init__(

            command_keyword="start".lower(),
            help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        mensaje ="""
         Hola y bienvenido seas al BoT GGs, aqui te muestro un pequeño menu
         de lo que puedo hacer, escribe el numero de la opcion que quieras
         usar:

        **Cambiar nombre a un dispositivo**

        Para usar esta opcion tienes que escribir: 
        Cambiar nombre + nuevo nombre del dispositivo + ip del dispositivo
            
        Ejemplo: Cambiar nombre R2 192.168.0.23

        **Crear loopback en un dispositivo.**

        Para usar esta opcion tienes que escribir:
        Crear loopback + numero de loopback + direccion ip de la loopback + submasck de la loopback.

        Ejemplo: Crear loopback 150 192.168.100.15 255.255.255.0     

        **Borrar loopback en un dispositivo.**

        Para usar esta opcion tienes que escribir:
        Borrar loopback + numero de la loopback

        Ejemplo: Borrar loopback 150

        **Mostrar interfaces de un dispositivo.

        Para usar esta opcion tienes que escribir: Ver interfaces

        """
        return mensaje



############################Cambiar Nombre############################



class CambiarNombre(Command):
    def __init__(self):
        super().__init__(
            command_keyword="cambiar nombre".lower()
        )
        print("2")
    
    def execute(self, message, attachment_actions, activity):
        datos = message.split()
        print(datos)

        n = datos[0]
        m = manager.connect(host=direccion_equipo,port=830,username=credenciales[0],password=credenciales[1],hostkey_verify=False)
        netconf_hostname = """
        <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>"""+n+"""</hostname>
        </native>
        </config>
        """
        netconf_reply = m.edit_config(target="running", config=netconf_hostname)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


############################Crear Loopbacks############################
class CrearLoopback(Command):
    def __init__(self):
        super().__init__(
            command_keyword="crear loopback".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        datos_loopback = message.split()
        print(datos_loopback)

        name = datos_loopback[0]
        ip = datos_loopback[1]
        mask = datos_loopback[2]

        m = manager.connect(host=direccion_equipo,port=830,username=credenciales[0],password=credenciales[1],hostkey_verify=False)

        netconf_newloop = """
        <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
        <Loopback>
            <name>"""+name+"""</name>
            <description>prueba</description>
            <ip>
            <address>
            <primary>
            <address>"""+ip+"""</address>
            <mask>"""+mask+"""</mask>
            </primary>
            </address>
            </ip>
        </Loopback>
        </interface>
        </native>
        </config>
        """
        netconf_reply = m.edit_config(target="running", config=netconf_newloop)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

############################ELIMINAR LOOPBACK############################

class BorrarLoopback(Command):
    def __init__(self):
        super().__init__(
            command_keyword="borrar loopback".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        deloop = message
        c = deloop.split()
        print (c)
        resp =  requests.delete('https://'+direccion_equipo+'/restconf/data/ietf-interfaces:interfaces/interface=Loopback'f'{c[0]}', auth=basicauth, headers=headers, verify=False)
        print(resp)
        return "La loopback "+deloop +" fue borrada exitosamente."


############################Ver Interfaces############################
class VerInterfces(Command):
    def __init__(self):
        super().__init__(
            command_keyword="ver interfaces".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        datos_loopback = message.split()
        print(datos_loopback)
        
        requests.packages.urllib3.disable_warnings()
        api_url = "https://"+direccion_equipo+"/restconf/data/ietf-interfaces:interfaces"
        
        resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
        print(resp)
        response_json = resp.json()
        a =json.dumps(response_json, indent=4)
        return a