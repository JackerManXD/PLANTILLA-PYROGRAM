from pyrogram import Client, filters
from os import getenv

api_hash = getenv("API_HASH")
api_id = getenv("API_ID")
bot_token = getenv("BOT_TOKEN")

try: from Debug import api_hash, api_id, bot_token
except: pass

bot = Client(name="name_bot", api_hash=api_hash, api_id=api_id, bot_token=bot_token)

# *************************************************************************** FUNCION START
@bot.on_message(filters.command('start'))
def start(bot, message):
    message.reply("Hola Pyrogram")

if __name__=='__main__':
    print("BOT EN EJECUCIÓN...")
    bot.run()