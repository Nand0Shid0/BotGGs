from ncclient import manager
import xml.dom.minidom
from webex_bot.models.command import Command
import json
import requests

requests.packages.urllib3.disable_warnings()

direccion_equipo = "172.16.100.40"
credenciales = ["cisco","cisco123!"]
basicauth = (credenciales[0], credenciales[1])


headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
}

############################MENU############################

class Menu(Command):
    def __init__(self):
        super().__init__(

            command_keyword="start".lower(),
            help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        mensaje ="""

         Hello and welcome to the BotGGs!
         Below is a small manual for the use of this bot, enjoy it!

        **Add user**

        To use this option you have to type:
        @BoT add_user + 'email@example.com'

        **Show_name**

        To use this option you have to type:
        @BoT show_name

        **Change device name**

        To use this option you have to type:
        @BoT + Change_name + new device name
            
        Example: @BoT Change name R2

        **Create loopback on the device.**

        To use this option you have to type:
        @BoT + Create_loopback + loopback number + ip address loopback + submasck loopback.

        Example: @BoT Create loopback 150 192.168.100.15 255.255.255.0

        **Delete loopback on the device.**

        To use this option you have to type:
        @BoT + Delete_loopback + loopback number

        Example: @BoT Delete loopback 150

        **Show interface on the device.**

        To use this option you have to type: @BoT Show_interface

        **Actuador**
        As an extra option, the use of an actuator was
        added to the bot, to use it you just have to type:

        @BoT Led On --> Will send a signal to an esp 32 to turn on a led.

        @BoT Led Off --> Will send a signal to an esp 32 to turn off a led.
        """
        return mensaje



############################Cambiar Nombre############################



class CambiarNombre(Command):
    def __init__(self):
        super().__init__(
            command_keyword="change_name".lower()
        )
    
    def execute(self, message, attachment_actions, activity):
        try:
            datos = message.split()
            print(datos)

            n = datos[2]
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
            return "The name change was successful."
        except:
            return "an error occurred, try again!."


############################Crear Loopbacks############################
class CrearLoopback(Command):
    def __init__(self):
        super().__init__(
            command_keyword="create_loopback".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        try:
            datos_loopback = message.split()
            print(datos_loopback)

            name = datos_loopback[2]
            ip = datos_loopback[3]
            mask = datos_loopback[4]

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
            return "The loopback "+name+" was create successful."
        except:
            return "an error occurred, try again!."


############################ELIMINAR LOOPBACK############################

class BorrarLoopback(Command):
    def __init__(self):
        super().__init__(
            command_keyword="delete_loopback".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        try:
            deloop = message
            c = deloop.split()
            print (c)
            resp =  requests.delete('https://'+direccion_equipo+'/restconf/data/ietf-interfaces:interfaces/interface=Loopback'f'{c[2]}', auth=basicauth, headers=headers, verify=False)
            print(resp)
            return "The loopback "+c[2]+" was delete successful."
        except:
            return "an error occurred, try again!."

class ShowName(Command):
    def __init__(self):
        super().__init__(
            command_keyword="Show_Name".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        try:
            resp =  requests.get('https://'+direccion_equipo+'/restconf/data/Cisco-IOS-XE-native:native/hostname', auth=basicauth, headers=headers, verify=False)
            response_json = resp.json()
            tmp = str(json.dumps(response_json, indent=4))
            return tmp      
        except:
            return "an error occurred, try again!."

############################Ver Interfaces############################
class VerInterfces(Command):
    def __init__(self):
        super().__init__(
            command_keyword="show_interface".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        try:
            datos_loopback = message.split()
            print(datos_loopback)

            requests.packages.urllib3.disable_warnings()
            api_url = "https://"+direccion_equipo+"/restconf/data/ietf-interfaces:interfaces"

            resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
            print(resp)
            response_json = resp.json()
            a =json.dumps(response_json, indent=4)
            return a
        except:
            return "an error occurred, try again!."

############################Actuador############################
class Esp32(Command):
    def __init__(self):
        super().__init__(
            command_keyword="Led".lower(),
        )
        
    def execute(self, message, attachment_actions, activity):
        datos_led = message.split()
        #print(datos_led)
        tmp = datos_led[2]
        tmp.lower()

        if tmp.lower() == 'on':
            print("entre al on")
            payload_led = {'led':'on'}
            led_r = requests.get(url = 'http://172.16.100.65/', params = payload_led)
            return "LED ON"  
        elif tmp.lower() == 'off':
            print("entre al off")
            payload_led = {'led':'off'}
            led_r = requests.get(url = 'http://172.16.100.65/', params = payload_led)
            return "LED OFF" 


######### AÑADIR USUARIO ##########
class AddUser(Command):
    def __init__(self):
        super().__init__(
            command_keyword="Add_user".lower(),
        )
    def execute(self, message, attachment_actions, activity):
        email = message.split()
        access_token="OWRmY2Q0ZTUtMzcwMy00YzA1LWFlNGUtY2UyMzdmMDBkMzNmYzk4NTJhMDItY2Rm_PF84_d3558e03-2933-4d83-8021-b115db9045d4"
        room_id= "Y2lzY29zcGFyazovL3VzL1JPT00vNWMyY2JhOTAtYjQzZS0xMWVjLWI0M2ItZDc3Yzg1OTNmYTIy"
        url = 'https://webexapis.com/v1/memberships'
        personEmail = email[2]
        print (personEmail)
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'personEmail': personEmail}
        res = requests.post(url, headers=headers, json=params)
        print(res.json())