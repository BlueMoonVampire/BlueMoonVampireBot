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
