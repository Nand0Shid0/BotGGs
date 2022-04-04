from webex_bot.webex_bot import WebexBot
from inf import *



#bot = WebexBot ('NmVhMTliM2ItODIzOS00ODExLWEwZDEtYzk3MTE4YWQwODZkNDczZDcwMTEtOTAz_PF84_2ec9c128-5f70-44f0-ac34-595d586542bb')
bot = WebexBot("ODQwMTVmYjUtMjFkYy00Y2Q3LTgyMDMtODhjZGFhMWVmZDdhYmMxZmNmNTQtZTA4_PF84_d3558e03-2933-4d83-8021-b115db9045d4")
#Clases para ver menus.

bot.add_command(Menu())

#Clases de configuracion.

bot.add_command(CambiarNombre())
bot.add_command(CrearLoopback())
bot.add_command(VerInterfces())
bot.add_command(BorrarLoopback())
bot.add_command(Esp32())
bot.run()
