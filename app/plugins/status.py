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
    if not role == "":
        db.add_role(m.from_user.id, role)
        m.reply("Done!")
    else:
        m.reply("Usage : /setrole role")
