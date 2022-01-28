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

from .. import bot
from ..utils import *
from ..db import DATABASE
from config import DEVS, MONGO_URI
from pyrogram import filters
from pyrogram.types import Message

db = DATABASE(MONGO_URI)

@bot.on_message(filters.command("status", ['/', ".", "?"]))
async def status(bot, m: Message):

    if m.from_user.id in DEVS:
        status = "**Clan Of BlueMoon**"

    elif db.get_role(m.from_user.id)['status'] != True:
        status = "Human"

    elif db.get_role(m.from_user.id)['status'] == True:
        status = db.get_role(m.from_user.id)['role']

    else:
        status = "Human"

    if m.from_user.id in DEVS:
        text = f"""
**Welcome Master {m.from_user.first_name}**

__The Vampire Of BlueMoon__

**Status** : **{status}**

**Use me to slay the CrimsonMoon**
"""

        await m.reply_photo("https://wallpaperaccess.com/full/6766185.jpg",
                            caption=text,
                            parse_mode="markdown")

    else:
        text = f"""
**Welcome {m.from_user.first_name}**,
**Status** : **{status}**
"""

        await m.reply(text, parse_mode="markdown")


@bot.on_message(filters.command("setrole"))
def setstatus(_, m: Message):
    role = m.text.replace(m.text.split(" ")[0], "")
    if role != "":
        db.add_role(m.from_user.id, role)
        m.reply("Done!")
    else:
        m.reply("Usage : /setrole role")
