from app import SYL, bot
from app import app
from config import DEVS, LOGS
from app.utils import *
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
import time
from pyrogram.types import Message




@bot.on_message(filters.command("ungscan", prefixes=["/", ".", "?", "-"]))
async def ungscan(bot: Client, m: Message):
    if not m.from_user.id in DEVS:
        await m.reply_text("Only Vampire of the Blue moon Can Use Me")

    if m.from_user.id in DEVS:
        i = await m.reply_text("Scanning...")
        grp = m.command[1]
        k = bot.iter_chat_members(grp, filter="administrators")
        users = []
        async for x in k:
            if not x.user.is_bot:
                users.append(x.user.id)
        await i.edit(f"{len(users)} Admins Found")
        await m.reply("Unbanning....")
        for x in users:
            try:
                SYL.unban(x)
                buttons = [[
                    InlineKeyboardButton("Support",
                                         url="https://t.me/Sylviorus_support"),
                ],
                           [
                               InlineKeyboardButton(
                                   "Report",
                                   url="https://t.me/SylviorusReport"),
                           ]]
                await bot.send_message(
                    LOGS,
                    f"""
#UNBANNED

**USER** : [{x}](tg://user?id={x})
**ENFORCER** : [{m.from_user.id}](tg://user?id={m.from_user.id})
**CHAT_ID** : {m.chat.id}
""",
                    reply_markup=InlineKeyboardMarkup(buttons))
                time.sleep(1)
            except Exception as e:
                await i.edit(f"{e}")
            except Floodwait as e:
                time.sleep(e.x)
        await m.reply("Done!")

