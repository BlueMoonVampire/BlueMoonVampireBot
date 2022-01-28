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


from pyrogram import filters
from .. import bot
from requests import get
from ..utils import *
from config import DEVS
from pyrogram.types import Message


def is_blacklisted(user):
    res = get("https://sylviorus-api.up.railway.app/user/" + str(user)).json()
    return bool(res['blacklisted'])


@bot.on_message(filters.new_chat_members)
def notify(_, m: Message):
    user = m.from_user.id
    if user in DEVS:
        m.reply("Welcome Dev {}".format(m.from_user.first_name))

    elif is_blacklisted(user):
        m.reply("This User Is Blacklisted!")
