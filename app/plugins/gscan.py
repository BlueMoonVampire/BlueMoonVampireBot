"""
MIT License
Copyright (C) 2021-2022, NkSama
Copyright (C) 2021-2022 Moezilla
Copyright (c) 2021, Sylviorus, <https://github.com/Sylviorus/BlueMoonVampireBot>
This file is part of @BlueMoonVampireBot (Antispam Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from app import SYL, bot
from app.utils import *
from config import DEVS, LOGS
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message


@bot.on_message(filters.command("gscan", prefixes=["/", ".", "?", "-"]))
async def gscan(bot: Client, m: Message):
    if m.from_user.id not in DEVS:
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
        await m.reply("Gbanned!")
