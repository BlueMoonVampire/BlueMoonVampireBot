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

from app import bot, SYL
from app.utils import check_dev,
from config import LOGS, DEVS
from app.utils import *
from pyrogram.types import Message
from pyrogram import filters, Client


@bot.on_message(filters.command("check", ['/', ".", "?"]))
async def check(bot: Client, m: Message):
    if not m.reply_to_message:
        user = m.command[1]
        if not user.isdigit():
            await m.reply_text("User ID Must Be Integer")
            return

        else:
            user = int(user)
            if user in DEVS:
                m.reply("This User Is My Captain")

            else:
                x = SYL.check(user)
                if x['blacklisted']:
                    await m.reply(f"""
#CHECK

**USER** : [{user}](tg://user?id={user})
**REASON** : {x["reason"]}
**ENFORCER** : [{x["enforcer"]}](tg://user?id={x["enforcer"]})
    """.strip())
                else:
                    await m.reply("This User Is Not Blacklisted")

    if m.reply_to_message:
        user = m.reply_to_message.from_user.id

        if user in DEVS:
            await m.reply("This User Is My Captain")

        else:
            x = SYL.check(user)
            await m.reply(f"""
#CHECK

**USER** : [{user}](tg://user?id={user})
**REASON** : {x["reason"]}
**ENFORCER** : [{x["enforcer"]}](tg://user?id={x["enforcer"]}""".strip())
