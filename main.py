from pyrogram import Client

api_id = 0
api_hash = ""
bot_token = ""

app = Client(
    "bot",
    api_id,
    api_hash,
    bot_token=bot_token,
    plugins={"root":"plugs/api"}
)

app.run()