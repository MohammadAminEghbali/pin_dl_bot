from pyrogram import Client, filters
from pyrogram.types import Message
from plugs.pin import download

from plugs.texts import caption, error

@Client.on_message(
    ~filters.edited &
    filters.regex(r"(pinterest\.com/pin/[^/]+|pin\.it/[^/]+)(/$|$)")
)

async def pin_dl(_, msg:Message) -> Message:
    url = f"https://{msg.matches[0].group(1)}"
        
    dl = download(url)
    if dl:
        send_type, url = dl
        if send_type == "gif":
            return await msg.reply_animation(url, caption=caption)
        
        elif send_type == "video":
            return await msg.reply_video(url, caption=caption)
        
        elif send_type == "image":
            return await msg.reply_photo(url, caption=caption)
            
    else:
        return await msg.reply_text(error)