import requests
import json

url = "https://172.16.100.34/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

basicauth = ("cisco", "cisco123!")


payload = {
   "interface": [
    {
      "name": "Loopback10000",
      "description": "Adding loopback10000",
      "type": "iana-if-type:softwareLoopback",
      "enabled": "true",
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.0.2.60",
            "netmask": "255.255.255.255"
          }
        ]
      }
    }
  ]
 }
requests.packages.urllib3.disable_warnings()
response = requests.post(url, headers=headers, data=json.dumps(payload), auth=basicauth, verify=False)


if (response.status_code == 201):
   print("Successfully added interface")
else:
   print("Issue with adding interface")
    