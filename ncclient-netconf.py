from ncclient import manager
import xml.dom.minidom


'''
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
print(capability)
'''
def filtro():
	netconf_filter = """
	<filter>
	<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
	</filter>
	"""
	netconf_reply = m.get_config(source="running", filter=netconf_filter)
	return print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def Nombre():
	name = input(str("ingresa el nuevo hostname: "))
	m = manager.connect(host="192.168.0.17",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

	netconf_hostname = """
	<config>
	<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname>"""+name+"""</hostname>
	</native>
	</config>
	"""
	netconf_reply = m.edit_config(target="running", config=netconf_hostname)
	print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def crear_loopback():

	#x = input(str("ingresa numero de loopback: "))
	#ip = input(str("ingresa direccion ip la de loopback: "))
	#mask = input(str("ingresa mascara de loopback: "))

	m = manager.connect(host="192.168.0.17",port=830,username="cisco",password="cisco123!",hostkey_verify=False)


	netconf_loopback = """
	<config>
	native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"
	<interface>
	<Loopback>
	<name>"""+"25"+"""</name>
	<description>Prueba</description>
	<ip>
	<address>
	<primary>
	<address>"""+"172.16.100.25"+"""</address>
	<mask>"""+"255.255.255.0"+"""</mask>
	</primary>
	</address>
	</ip>
	</Loopback>
	</interface>
	</native>
	</config>
	"""
	netconf_reply = m.edit_config(target="running", config=netconf_loopback)
	print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

Nombre()




