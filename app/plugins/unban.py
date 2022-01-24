from app import bot, SYL
from app import app
from config import DEVS, LOGS
from app.utils import check_dev
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters, Client


@bot.on_message(filters.command("sylunban", ['/', ".", "?"]))
async def unban(bot: Client, m: Message):
    if not m.from_user.id in DEVS:
        await m.reply_text("Only Captain Can Use Me")
        return

    if m.from_user.id in DEVS and not m.reply_to_message:
        user = m.command[1]
        if not user.isdigit():
            await m.reply_text("User ID Must Be Integer")
            return

        else:
            user = int(user)
            if user not in DEVS:
                x = SYL.unban(user)
                await m.reply(x)
            else:
                await m.reply("Captain Cant Be Unbanned!")

    if m.from_user.id in DEVS and m.reply_to_message:
        user = m.reply_to_message.from_user.id
        if not user in DEVS:
            user = int(user)
            x = SYL.unban(user)
            buttons = [[
                InlineKeyboardButton("Support",
                                     url="https://t.me/Sylviorus_support"),
            ],
                       [
                           InlineKeyboardButton(
                               "Report", url="https://t.me/SylviorusReport"),
                       ]]

            await bot.send_message(LOGS,
                                   f"""
#UNBANNED

**USER** : [{user}](tg://user?id={user})
**ENFORCER** : [{m.from_user.id}](tg://user?id={m.from_user.id})
**CHAT_ID** : {m.chat.id}
""",
                                   reply_markup=InlineKeyboardMarkup(buttons))
            await m.reply(x)

        else:
            await m.reply("Captain Cant Be Unbanned!")
