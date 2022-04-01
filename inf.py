from ncclient import manager
import xml.dom.minidom
from click import command
from webex_bot.models.command import Command
import json
import requests


requests.packages.urllib3.disable_warnings()

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
}
basicauth = ("cisco", "cisco123!")


class Hola(Command):
    def __init__(self):
        super().__init__(
            command_keyword="hola",
            help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        a = message
        print (a)
        return "Hola Humano" + a

class CambiarNombre(Command):
    def __init__(self):
        super().__init__(
            command_keyword="cambiar nombre",
        )
    def execute(self, message, attachment_actions, activity):
        nombres = message.split()
        print(nombres)
        n = nombres[0]
        m = manager.connect(host="192.168.0.17",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
        netconf_hostname = """
        <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>"""+n+"""</hostname>
        </native>
        </config>
        """
        netconf_reply = m.edit_config(target="running", config=netconf_hostname)
        print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



class CrearLoopback(Command):
    def __init__(self):
        super().__init__(
            command_keyword="loopback",
        )
    def execute(self, message, attachment_actions, activity):
        datos_loopback = message.split()
        print(datos_loopback)

        loop_back_name= datos_loopback[0]
        ip = datos_loopback[1]
        mask = datos_loopback[2]

        api_url = 'https://192.168.0.17/restconf/data/ietf-interfaces:interfaces/interface={}'.format(datos_loopback[0])
        
        yangConfig = {
            "ietf-interfaces:interface": {
                "name": loop_back_name,
                "description": "Loopback de Webex",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": ip,
                            "netmask": mask
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        }
        
        resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
        else:
            print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))