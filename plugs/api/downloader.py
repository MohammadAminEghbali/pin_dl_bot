from plugs.pin import download
from plugs.texts import caption, error, waiting_text
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    ~filters.edited &
    filters.regex(r"(pinterest\.com/pin/[^/]+|pin\.it/[^/]+)(/$|$)")
)

async def pin_dl(_, msg:Message) -> Message:
    url = f"https://{msg.matches[0].group(1)}"
    msg_tmp:Message = await msg.reply(waiting_text)
    
    dl = download(url)
    if dl:
        send_type, url = dl
        await msg_tmp.edit("**__Uploading to telegram__**")
        if send_type == "gif":
            await msg.reply_animation(url, caption=caption, reply_to_message_id=msg.message_id)
        
        elif send_type == "video":
            await msg.reply_video(url, caption=caption, reply_to_message_id=msg.message_id)
        
        elif send_type == "image":
            await msg.reply_photo(url, caption=caption, reply_to_message_id=msg.message_id)
        
        return await msg_tmp.delete()
            
    else:
        return await msg.reply_text(error)
