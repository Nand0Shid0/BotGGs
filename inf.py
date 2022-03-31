from webex_bot.models.command import Command
import json
import requests

#api_url = "https://192.168.1.99/restconf/data/ietf-interfaces:interfaces"

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
'''
class Interfaces (Command):
    def __init__(self):
        super().__init__(
            command_keyword="interfaces",
        )
    def execute(self, message, attachment_actions, activity):
        resp =  requests.get(api_url, auth=basicauth, headers=headers, verify=False)
        response_json = resp.json()
        r = str(json.dumps(response_json, indent=4))
        return r + "\n SERVIDO JEFE......."
'''

class loopback (Command):
    def __init__(self):
        super().__init__(
            command_keyword="loopback",
            help_message="Get current weather conditions by ZIP code.",
        )

        
    def execute(self, message, attachment_actions, activity):
        datos = message.split(sep=',')
        api_url = "https://172.16.100.170/restconf/data/ietfinterfaces:interfaces/interface=Loopback{}".format(datos[0])
        yangConfig = {
            "ietf-interfaces:interface": {
                "name": "Loopback{}".format(datos[0]),
                "description": "My second RESTCONF loopback",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "{}".format(datos[1]),
                            "netmask": "{}".format(datos[2])

                            }
                        ]
                    },
                "ietf-ip:ipv6": {}
                }
            }
        resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
        

