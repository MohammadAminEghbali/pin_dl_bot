from pyrogram import Client, filters
from pyrogram.types import Message
from plugs.texts import start_text

@Client.on_message(
    ~filters.edited &
    filters.command("start")
)

async def start(_, msg:Message) -> Message:
    return await msg.reply(start_text)