import os
import random
import aiofiles
import aiohttp
from os import path
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from vanitas import User as vanitas
from .. import bot
from time import time
from pyrogram.types import ChatPermissions
from requests import get
from ..utils import DEVS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message



async def blacklistimage(enforcer, title, user, reason, vanitasimage):
    async with aiohttp.ClientSession() as session:
        async with session.get(vanitasimage) as resp:
            if resp.status == 200:
                f = await aiofiles.open("report.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./report.png")
    image2 = image1.convert("RGBA")
    Image.alpha_composite(image2).save("save.png")
    i = Image.open("save.png")
    draw = ImageDraw.Draw(i)
    font = ImageFont.truetype("app/fonts.otf", 32)
    draw.text(
        (205, 590),
        f"USER: {user} | {title}",
        fill="white",
        stroke_width=1,
        stroke_fill="black",
        font=font,
    )
    draw.text(
        (205, 630),
        f"REASON: {reason}",
        fill="white",
        stroke_width=1,
        stroke_fill="black",
        font=font,
    )
    draw.text(
        (205, 670),
        f"ENFORCER: {enforcer}",
        fill="white",
        stroke_width=1,
        stroke_fill="black",
        font=font,
    )
    i.save("vanitas.png")
    os.remove("save.png")
    os.remove("report.png")


v = vanitas()


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
    if is_admin(query.from_user.id,
                query.message.chat.id) and query.data.split(":")[1] == "mute":
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


@bot.on_message(filters.new_chat_members)
async def alert(_, m: Message):
    user = m.from_user.id
    x = v.get_info(user)
    if x.blacklisted:
        vanitasimage = "https://telegra.ph/file/c4bcc673963abc4fdb137.jpg"
        user = user
        title = m.from_user.first_name
        reason = x.reason
        enforcer = x.enforcer
        await blacklistimage(enforcer, title, user, reason, vanitasimage)
        await m.reply_photo(
            photo="vanitas.png",
            caption=
            f"#ALERT\n**This User Is Blacklisted**\n**USER** : [{user}](tg://user?id={user})\n**REASON** : {x.reason}\n**ENFORCER** : [{x.enforcer}](tg://user?id={x.enforcer})",
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
