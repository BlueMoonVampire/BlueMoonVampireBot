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

import imp
from app import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.utils import *

HELP_TEXT = """
**COMMANDS** :  

**Human Commands** :

/start - __Start Mesasage__
/help - __Help Message__
/check userid or reply to user - __Check User__
/setrole - __Roles Name__
/sylreport - __Report Message__

**Clan Of BlueMoon Commands**:

/scan userid __reason or reply to user__ - __Ban User__
/scanunban userid - __Unban User__
/gscan Username - __All Group Admin Ban__
/ungscan Username - __All Group Admin Unban__
"""


@bot.on_message(filters.command("help", ['/', ".", "?"]))
async def help(bot, m):
    await m.reply(HELP_TEXT,
                  parse_mode="markdown",
                  reply_markup=InlineKeyboardButton([[
                      InlineKeyboardButton(
                          "Support", url="https://t.me/sylviorus_support")
                  ]]))
