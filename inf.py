from webex_bot.models.command import Command

import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.1.99/restconf/data/ietf-interfaces:interfaces"

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
        return "Hola Humano"



class Interfaces (Command):
    def __init__(self):
        super().__init__(
            command_keyword="interfaces",
            help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        rresp =  requests.get(api_url, auth=basicauth, headers=headers, verify=False)
        response_json = rresp.json()
        r = str(json.dumps(response_json, indent=4))
        return r