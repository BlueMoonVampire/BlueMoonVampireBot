from app import SYL, bot
from app import app
from app.utils import *
from config import DEV, LOGS
from pyrogram import filters
from pyrogram.errors import FloodWait
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


@bot.on_message(filters.command("gscan", prefixes=["/", ".", "?", "-"]))
async def gscan(bot: Client, m: Message):
    if not m.from_user.id in DEVS:
        await m.reply_text("Only Vampire of the Blue moon Can Use Me")

    if m.from_user.id in DEVS:
        i = await m.reply_text("Scanning...")
        grp = m.command[1]
        k = bot.iter_chat_members(grp, filter="administrators")
        users = []
        async for x in k:
            if not x.user.is_bot:
                users.append(x.user.id)
        await i.edit(f"{len(users)} Admins Found")
        await m.reply("Banning....")
        for x in users:
            try:
                SYL.ban(x, "Mass Adder MSG_ID : {}".format(m.message_id),
                        m.from_user.id)
                buttons = [[
                    InlineKeyboardButton("Support",
                                         url="https://t.me/Sylviorus_support"),
                ],
                           [
                               InlineKeyboardButton(
                                   "Report",
                                   url="https://t.me/SylviorusReport"),
                           ]]
                await bot.send_message(
                    LOGS,
                    f"""
#BANNED

**USER** : [{x}](tg://user?id={x})
**REASON**: MASS ADDING For @{grp}
**ENFORCER** : [{m.from_user.id}](tg://user?id={m.from_user.id})
**CHAT_ID** : {m.chat.id}
""",
                    reply_markup=InlineKeyboardMarkup(buttons))
                time.sleep(1)
            except Exception as e:
                await i.edit(f"{e}")
            except Floodwait as e:
                time.sleep(e.x)
        await m.reply("Done!")
