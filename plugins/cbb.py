#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>𝖡𝖮𝖳 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌\n❏ 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖥𝗈𝗋 𝖡𝖮𝖳 𝖠𝖽𝗆𝗂𝗇𝗌\n├/start : start the bot or get posts\n├/batch : Create Group Message\n├/genlink : create link for one post\n├/users : view bot statistics\n├/broadcast : broadcast Message\n└/stats : checking your bot uptime\n\n👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝖽 𝖻𝗒 <a href=https://t.me/AnimeDiversity>𝖠𝗇𝗂𝗆𝖾 𝖣𝗂𝗏𝖾𝗋𝗌𝗂𝗍𝗒</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥ᴄʟᴏꜱᴇ💥", callback_data="close"),
                        InlineKeyboardButton("⚡ᴀʙᴏᴜᴛ⚡", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>Hi there this is a file store bot which is convert any file to link...\nthen you can access this file through a specific link...!\n\nMy Channel <a href=https://t.me/AnimeDiversity>𝖠𝗇𝗂𝗆𝖾 𝖣𝗂𝗏𝖾𝗋𝗌𝗂𝗍𝗒</a>\n\n👨‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝖽 𝖻𝗒 <a href=https://t.me/AnimeDiversity>𝖠𝗇𝗂𝗆𝖾 𝖣𝗂𝗏𝖾𝗋𝗌𝗂𝗍𝗒</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥ᴄʟᴏꜱᴇ💥", callback_data="close"),
                        InlineKeyboardButton("🚀ʜᴇʟᴘ🚀", callback_data="help")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
