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

/sylban userid __reason or reply to user__ - __Ban User__
/sylunban userid - __Unban User__
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
