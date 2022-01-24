from pyrogram import filters
from .. import bot
from requests import get
from ..utils import *
from config import DEVS
from pyrogram.types import Message


def is_blacklisted(user):
    res = get("https://sylviorus-api.up.railway.app/user/" + str(user)).json()
    return True if res['blacklisted'] else False


@bot.on_message(filters.new_chat_members)
def notify(_, m: Message):
    user = m.from_user.id
    if user in DEVS:
        m.reply("Welcome Dev {}".format(m.from_user.first_name))

    elif is_blacklisted(user):
        m.reply("This User Is Blacklisted!")

    else:
        pass
