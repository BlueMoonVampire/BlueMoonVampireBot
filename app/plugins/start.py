from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app import bot
from app import app
from app.utils import *

sylmessage = '''
Hi, Welcome {}
'''


@bot.on_message(filters.command(["start"], ['/', ".", "?"]))
async def start(client, message):
    buttons = [[
        InlineKeyboardButton("Support", url="https://t.me/Sylviorus_support"),
    ]]
    await message.reply_text(sylmessage.format(message.from_user.first_name),
                             reply_markup=InlineKeyboardMarkup(buttons))
