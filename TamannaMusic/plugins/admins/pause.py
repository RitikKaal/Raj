from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PickUpLineMusic import app
from PickUpLineMusic.core.call import romaan
from PickUpLineMusic.utils.database import is_music_playing, music_off
from PickUpLineMusic.utils.decorators import AdminRightsCheck
from PickUpLineMusic.utils.inline import close_markup
from config import BANNED_USERS

@app.on_message(filters.command(["pause", "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await romaan.pause_stream(chat_id)
    
    buttons = [
        [
            InlineKeyboardButton(text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
    ]
    
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons)
    )
