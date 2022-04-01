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
	#name = input(str("ingresa el nuevo hostname: "))
	m = manager.connect(host="192.168.0.23",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

	netconf_hostname = """
	<config>
	<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<command>"""+"do show ip int brief"+"""</command>
	</native>
	</config>
	"""
	netconf_reply = m.edit_config(target="command", config=netconf_hostname)
	print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def crear_loopback():

	x = input(str("ingresa numero de loopback: "))
	ip = input(str("ingresa direccion ip la de loopback: "))
	mask = input(str("ingresa mascara de loopback: "))

	m = manager.connect(host="192.168.0.23",port=830,username="cisco",password="cisco123!",hostkey_verify=False)


	netconf_newloop = """
	<config>
	 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	  <interface>
	   <Loopback>
	    <name>"""+x+"""</name>
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

def borrar_loopback():
	x = input(str("ingresa numero de loopback: "))
	m = manager.connect(host="192.168.0.23",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

	netconf_borrar_loopback ="""
	<config>
	 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	  <interface>
	   <Loopback>
	    <name>"""+x+"""</name>
	    <description></description>
	    <ip>
	     <address>
	      <primary>
	       <address></address>
	       <mask></mask>
	      </primary>
	     </address>
	    </ip>
	   </Loopback>
	  </interface>
	 </native>
	</config>
	"""
	netconf_reply = m.edit_config(target="running", config=netconf_borrar_loopback)
	print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


Nombre()
#crear_loopback()
#borrar_loopback()



