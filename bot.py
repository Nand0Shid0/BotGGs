from webex_bot.webex_bot import WebexBot
from inf import *


bot = WebexBot ('ODQwMTVmYjUtMjFkYy00Y2Q3LTgyMDMtODhjZGFhMWVmZDdhYmMxZmNmNTQtZTA4_PF84_d3558e03-2933-4d83-8021-b115db9045d4')
bot.add_command(Interfaces())
bot.add_command(Hola())

bot.run()