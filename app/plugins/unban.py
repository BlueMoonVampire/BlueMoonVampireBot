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
from config import DEVS, LOGS
from app.utils import check_dev
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters, Client


@bot.on_message(filters.command("unscan", ['/', ".", "?"]))
async def unban(bot: Client, m: Message):
    if m.from_user.id not in DEVS:
        await m.reply_text("Only Captain Can Use Me")
        return

    if not m.reply_to_message:
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
        if user not in DEVS:
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
