from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

app = Client("my_bot", api_id=0, api_hash="your_hash",
             bot_token="your_bot_token")


@app.on_message(filters.group & filters.text & filters.regex(r"@all"))
async def save_members(client: Client, message: Message):
    chat_id = message.chat.id

    message_text = "**Mention ALL🔔**"
    async for member in client.get_chat_members(chat_id):
        hidden_tag = f"[​](tg://user?id={member.user.id})\u200B"
        message_text += hidden_tag

    while message_text:
        await message.reply(message_text[:4096], parse_mode=ParseMode.DEFAULT)
        message_text = message_text[4096:]


app.run()
