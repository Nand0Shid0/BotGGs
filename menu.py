from click import command
from webex_bot.models.command import Command



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
               
        1.- Cambiar nombre a un dispositivo.
        2.- Crear una loopback
        3.- Obtener interfaces de un dispositivo.
        4.- Encender un led.
        """
        return mensaje

class opcion1(Command):
    def __init__(self):
        super().__init__(
        command_keyword="1",
        help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        print(message)
        if message == "1":

            mensaje ="""
                **Cambiar nombre a un dispositivo**

            Con esta opcion podras renombrar a un router, las credenciales ya
            fueron introducidas con anterioridad.

            Para usar esta opcion tienes que escribir: Cambiar nombre + nuevo nombre del dispositivo
            
            Ejemplo: Cambiar nombre R2 192.168.0.23

            """
            return mensaje

class opcion2(Command):
    def __init__(self):
        super().__init__(
        command_keyword="2",
        help_message="Get current weather  by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        mensaje ="""
         **Crear una loopback en un dispositivo**

        Con esta opcion podras crear una interface virtual para pruebas, las credenciales ya
        fueron introducidas    def execute(self, message, attachment_actions, activity):
        con anterioridad.

        Para usar esta opcion tienes que escribir: 
        Crear loopback + N°de loopback + ip de la loopback + mascara de la loopback + direccion ip del dispositivo.
        
        Ejemplo: Cambiar nombre R1 192.168.0.23

        """
        return mensaje



class opcion3(Command):
    def __init__(self):
        super().__init__(
        command_keyword="3",
        help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        mensaje ="""
         **Obtener interfaces de un dispositivo.**

        Con esta opcion podras obtener informacion sobre las interfaces de un router, las credenciales ya
        fueron introducidas con anterioridad.

        Para usar esta opcion tienes que escribir: Ver interfaces + ip del dispositivo
        
        Ejemplo: Ver interfaces 192.168.0.23

        """
        return mensaje

class opcion4(Command):
    def __init__(self):
        super().__init__(

            command_keyword="4",
            help_message="Get current weather conditions by ZIP code.",
        )
    def execute(self, message, attachment_actions, activity):
        mensaje ="""
         **Encender un led.**

        
         

        """
        return mensaje


