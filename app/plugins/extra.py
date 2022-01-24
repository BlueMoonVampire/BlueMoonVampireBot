from .. import bot
from config import DEVS
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from requests import get, post
from subprocess import getoutput as run


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"


@bot.on_message(
    filters.command("logs", prefixes=['.', '/', ';', ','
                                      '*']) & filters.user(DEVS))
def sendlogs(_, m: Message):
    logs = run("tail logs.txt")
    x = paste(logs)
    keyb = [
        [
            InlineKeyboardButton("SpaceBin", url=x),
            InlineKeyboardButton("Send", callback_data="sendfile")
        ],
    ]
    m.reply(x,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(keyb))


@bot.on_callback_query(filters.regex(r"sendfile"))
def sendfilecallback(_, query: CallbackQuery):
    sender = query.from_user.id
    chat = query.message.chat.id

    if sender in DEVS:
        query.message.edit("Sending Logs file..")
        query.message.reply_document("logs.txt")

    else:
        query.answer("Only Devs can use me")


@bot.on_message(filters.command("id", prefixes=['.', "/", "?", ";"]))
def tg_id(_, m: Message):
    if m.reply_to_message:
        user = m.reply_to_message.from_user.id
        info = bot.get_users(user)
        m.reply_text(
            f"**{info.first_name}'s** Id : ```{info.id}```\n**Your Id** : ```{m.from_user.id}```\n**Chat Id** : ```{m.chat.id}```"
        )

    elif len(m.command) == 2:
        user = m.command[1]
        info = bot.get_users(user)
        m.reply_text(
            f"**{info.first_name}'s** Id : ```{info.id}```\n**Your Id** : ```{m.from_user.id}```\n**Chat Id** : ```{m.chat.id}```"
        )

    else:
        m.reply("Invalid Syntax")
