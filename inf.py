from webex_bot.models.command import Command
import json
import requests

api_url = "https://sandbox-iosxe-recomm-1.cisco.com/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

basicauth = ("developer", "C1sco12345")


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

class loopback (Command):
    def __init__(self):
        super().__init__(
            command_keyword="loopback",
            help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        a = message
        