from plugs.texts import help_text
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    ~filters.edited &
    filters.command("help")
)

async def helper(_, msg:Message) -> Message:
    return await msg.reply(help_text, disable_web_page_preview=True)
