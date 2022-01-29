
from pyrogram import filters
from vanitas import User as vanitas
from time import time
from pyrogram.types import ChatPermissions
from requests import get
from ..utils import DEVS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
from app.plugins.status import db

v = vanitas()


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
def kick_callback(_, query):
    user = query.data.split(":")[2]
    if is_admin(query.message.chat.id,
                query.from_user.id) and query.data.split(":")[1] == "kick":
        bot.ban_chat_member(query.message.chat.id, user)
        bot.unban_chat_member(query.message.chat.id, user)
        query.answer('Kicked!')
        query.message.edit(
            f'Kick User [{user}](tg://user?id={user})\n Admin User [{query.from_user.id}](tg://user?id={query.from_user.id})',
            parse_mode='markdown')
    else:
        message.reply('You are not admin!')


@bot.on_callback_query(call_back_filter("ban"))
def ban_callback(_, query):
    user = query.data.split(":")[2]
    if is_admin(query.message.chat.id,
                query.from_user.id) and query.data.split(":")[1] == "ban":
        bot.ban_chat_member(query.message.chat.id, user)
        query.answer('Banned')
        query.message.edit(
            f'Banned User [{user}](tg://user?id={user})\n Admin User [{query.from_user.id}](tg://user?id={query.from_user.id})',
            parse_mode='markdown')
    else:
        message.reply('You are not admin!')


@bot.on_callback_query(call_back_filter("mute"))
def mute_callback(_, query):
    user = query.data.split(":")[2]
    if is_admin(query.message.chat.id,
                query.from_user.id) and query.data.split(":")[1] == "mute":
        bot.restrict_chat_member(
            query.message.chat.id,
            user,
            ChatPermissions(can_send_messages=False),
        )
        query.answer('Muted!')
        query.message.edit(
            f'Muted User [{user}](tg://user?id={user})\n Admin User [{query.from_user.id}](tg://user?id={query.from_user.id})',
            parse_mode='markdown')
    else:
        message.reply('You are not admin!')


@bot.on_message(
    filters.command("alertmode", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def alertmode(_, message):
    if is_admin(message.user.id, message.chat.id):
        return
    is_vanitas = db.is_vanitas(message.chat.id)
    if not is_vanitas:
        db.set_vanitas(message.chat.id)
        await message.reply_text("Alert Mode Enable")
    else:
        db.rm_vanitas(message.chat.id)
        await message.reply_text("Alert Mode Disable")


@bot.on_message(filters.new_chat_members)
def alert(_, m: Message):
    user = m.from_user.id
    is_vanitas = db.is_vanitas(m.chat.id)
    if not is_vanitas:
        return
    if is_blacklisted(user):
        x = v.get_info(user)
        bot.send_message(
            m.chat.id,
            f"""
#ALERT
**This User Is Blacklisted**
**USER** : [{user}](tg://user?id={user})
**REASON** : {x.reason}
**ENFORCER** : [{x.enforcer}](tg://user?id={x.enforcer})""",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Ban",
                                         callback_data=f"ban:ban:{user}"),
                    InlineKeyboardButton("Kick",
                                         callback_data=f"kick:kick:{user}"),
                    InlineKeyboardButton("Mute",
                                         callback_data=f"mute:mute:{user}")
                ],
            ]))
    else:
        pass
