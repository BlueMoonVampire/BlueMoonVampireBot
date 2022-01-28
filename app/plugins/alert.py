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
from .. import bot, SYL
from requests import get
from ..utils import DEVS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
from app.plugins.token import db


def is_blacklisted(user):
    res = get("https://vanitas-api.up.railway.app/user/" + str(user)).json()
    return True if res['blacklisted'] else False


def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        if user_data.status == 'administrator' or user_data.status == 'creator':
            return True
        else:
            return False
    except:
        return False


def call_back_filter(data):
    return filters.create(lambda flt, _, query: flt.data in query.data,
                          data=data)


@bot.on_callback_query(call_back_filter("kick"))
def ban_callback(_, query):
    user = query.data.split(":")[2]
    if is_admin(query.message.chat.id,
                query.from_user.id) and query.data.split(":")[1] == "kick":
        bot.ban_chat_member(query.message.chat.id, user)
        bot.unban_chat_member(query.message.chat.id, user)
        query.answer('Kicked!')
        query.message.reply(
            f'Banned [{user}](tg://user?id={user})\n From [{query.from_user.id}](tg://user?id={query.from_user.id})',
            parse_mode='markdown')
    else:
        message.reply('You are not admin!')


@bot.on_message(filters.new_chat_members)
def alert(_, m: Message):
    user = m.from_user.id
    if is_blacklisted(user):
        x = SYL.check(user)
        bot.send_message(m.chat.id,
                         f"""
#ALERT
**USER** : [{user}](tg://user?id={user})
**REASON** : {x["reason"]}
**ENFORCER** : [{x["enforcer"]}](tg://user?id={x["enforcer"]})""",
                         reply_markup=InlineKeyboardMarkup([
                             [
                                 InlineKeyboardButton(
                                     "Kick", callback_data=f"kick:kick:{user}")
                             ],
                         ]))
    else:
        pass
