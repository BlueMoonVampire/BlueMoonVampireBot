from .. import bot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from ..utils import *
from config import DEVS, REPORT_LOGS
from requests import post, get
from .. import bot, SYL, ldb, app


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"{res.json()['payload']['id']}"


@bot.on_message(filters.command("sylreport"))
def report(_, m: Message):
    try:
        if m.reply_to_message and m.reply_to_message.from_user.id not in DEVS:
            m.reply("Report Sent")
            user = m.reply_to_message.from_user.id
            reason = m.text.replace(m.text.split(" ")[0], "")
            x = m.reply_to_message.forward(-1001774528355)
            enforcer = m.from_user.id
            keyb = []
            keyb.append([
                InlineKeyboardButton("BAN",
                                     callback_data=f"bam:accept:{user}:"),
                InlineKeyboardButton("UNBAN",
                                     callback_data=f"bam:reject:{user}")
            ])
            ldb.add_reason(user, reason)
            bot.send_message(REPORT_LOGS,
                             f"""
    #REPORT 
    **From** : [{m.from_user.id}](tg://user?id={m.from_user.id})
    **User** : [{user}](tg://user?id={user})
    **Chat** : {m.chat.id}
    **Message** : {m.reply_to_message.text}
    **Chat Username** : {m.chat.username}
    **Reason** : {reason}
    """,
                             reply_markup=InlineKeyboardMarkup(keyb))

    except Exception as e:
        m.reply(f"{e}")

    if m.reply_to_message.from_user.id in DEVS:
        m.reply("Vampire of the Blue moon Cant Be Reported!")


@bot.on_callback_query(filters.regex(r'bam'))
def bam_callback(_, query: CallbackQuery):
    data = query.data.split(":")
    if data[1] == "accept" and query.from_user.id in DEVS:
        user = int(data[2])
        msg = ldb.get_reason(str(user))
        SYL.ban(user, msg, query.from_user.id)
        buttons = [[
            InlineKeyboardButton("Support",
                                 url="https://t.me/Sylviorus_support"),
        ],
                   [
                       InlineKeyboardButton(
                           "Report", url="https://t.me/SylviorusReport"),
                   ]]
        bot.send_message(LOGS,
                         f"""
#BANNED

**USER** : [{user}](tg://user?id={user})
**ENFORCER** : [{query.from_user.id}](tg://user?id={query.from_user.id})
**REASON** : {msg}
**CHAT_ID** : {query.message.chat.id}
""",
                         reply_markup=InlineKeyboardMarkup(buttons))

    elif data[1] == "reject" and query.from_user.id in DEVS:
        user = int(data[2])
        buttons = [[
            InlineKeyboardButton("Support",
                                 url="https://t.me/Sylviorus_support"),
        ],
                   [
                       InlineKeyboardButton(
                           "Report", url="https://t.me/SylviorusReport"),
                   ]]
        SYL.unban(user)       
        bot.send_message(LOGS,
                         f"""
#UNBANNED

**USER** : [{user}](tg://user?id={user})
**ENFORCER** : [{query.from_user.id}](tg://user?id={query.from_user.id})
**CHAT_ID** : {query.message.chat.id}
""",
                         reply_markup=InlineKeyboardMarkup(buttons))

    if not query.from_user.id in DEVS:
        query.answer("You are not Vampire of The Blue Moon")
