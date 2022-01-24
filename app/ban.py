from app import SYL, bot
from app import app
from config import LOGS, DEV
from app.utils import *
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message


@bot.on_message(filters.command("sylban", prefixes=["/", ".", "?", "-"]))
async def ban(Client, m: Message):
    if not m.from_user.id in DEVS:
        await m.reply_text("Only The Vampire of Blue moon Can Use Me")

    if m.from_user.id in DEVS and not m.reply_to_message:
        user = m.command[1]
        reason = m.text.replace(m.text.split(" ")[0], "").replace(user, "")
        enforcer = m.from_user.id

        if len(user) != 10:
            await m.reply_text("Invalid id")
            return

        if not user.isdigit():
            await m.reply_text("User ID Must Be Integer")
            return

        else:
            user = int(user)
            if user not in DEVS:
                x = SYL.ban(user, reason, enforcer)
                buttons = [
                    [
                        InlineKeyboardButton(
                            "Support", url="https://t.me/Sylviorus_support")
                    ],
                    [
                        InlineKeyboardButton(
                            "Report", url="https://t.me/SylviorusReport")
                    ],
                ]

                await bot.send_message(
                    LOGS,
                    f"""
#BANNED
**USER**: [{user}](tg://user?id={user})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={enforcer})
**CHAT_ID** : {m.chat.id}
""",
                    reply_markup=InlineKeyboardMarkup(buttons))
                await m.reply(x)
            else:
                await m.reply("Vampires Cant Be Banned!")

    if m.from_user.id in DEVS and m.reply_to_message:
        user = m.reply_to_message.from_user.id
        reason = m.text.replace(m.text.split(" ")[0], "")
        enforcer = m.from_user.id

        if not user in DEVS:
            user = int(user)
            buttons = [[
                InlineKeyboardButton("Support",
                                     url="https://t.me/Sylviorus_support"),
            ],
                       [
                           InlineKeyboardButton(
                               "Report", url="https://t.me/SylviorusReport"),
                       ]]
            x = SYL.ban(user, reason, enforcer)
            await bot.send_message(LOGS,
                                   f"""
#BANNED

**USER**: [{user}](tg://user?id={user})
**REASON**: {reason}
**ENFORCER**: [{enforcer}](tg://user?id={enforcer})
**CHAT_ID** : {m.chat.id}
**Message Link : {m.link}
""",
                                   reply_markup=InlineKeyboardMarkup(buttons))
            await m.reply(x)

        else:
            await m.reply("The Vampire of Blue moon can't be banned!")
