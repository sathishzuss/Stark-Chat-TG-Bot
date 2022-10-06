import os
from StarkChat import starkchat
from pyrogram import *
from pyrogram.types import *

chatbot = starkchat.StarkChat()

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)  
CHAT_ID = os.environ.get("CHAT_ID", None) 

bot = Client("STARK", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.text)
async def response(client, message):
        question = message.text
        reply = chatbot.chat(question)
        await message.reply(reply)
        TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`"
        await bot.send_message(chat_id=CHAT_ID,text=TEXT)


def main():
     bot.run()


if __name__ == "__main__":
     main()
