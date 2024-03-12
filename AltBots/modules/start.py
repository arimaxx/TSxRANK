import asyncio
from datetime import datetime
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Filters

@app.on_message()
async def handle_messages(_, message):
    user_id = message.from_user.id
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1

    today_start = datetime.combine(datetime.today(), datetime.min.time())
    top_members_collection.update_one(
        {"_id": user_id},
        {"$inc": {"total_messages": 1}, "$set": {"last_updated": datetime.now()}},
        upsert=True
    )

@app.on_message(filters.private & filters.command("start"))
async def start_private_chat(client, message):
    # Choose a random image URL
    image_url = random.choice(IMAGE_URLS)

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️‍🔥ᴀᴅᴅ ᴍᴇ❤️‍🔥", url=f"t.me/{BOT_USERNAME}?startgroup=true"),
                InlineKeyboardButton("💫ꜱᴜᴘᴘᴏʀᴛ💫", url=f"t.me/{SUPPORT_GROUP_USERNAME}"),
            ],
            [
                InlineKeyboardButton("💖ꜱᴏᴜʀᴄᴇ💖", url=f"t.me/{SOURCE_CODE_CHANNEL_USERNAME}"),
            ]
        ]
    )

    await client.send_photo(
        chat_id=message.chat.id,
        photo=image_url,
        caption="<b>нυι</b> тнιѕ ιѕ 「🛡ᴛꜱ ʀᴀɴᴋɪɴɢ ʙᴏᴛ🛡」❖ 💖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n"
                "💫 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛꜱ ʀᴀɴᴋɪɴɢ ʙᴏᴛ!.\n "
                "🌟 ᴅɪꜱᴄᴏᴠᴇʀ ᴡʜᴏ ꜱʜɪɴᴇꜱ ᴛʜᴇ ʙʀɪɢʜᴛᴇꜱᴛ ɪɴ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ! ꜰʀᴏᴍ ᴀᴄᴛɪᴠᴇ ᴍᴇᴍʙᴇʀꜱ ᴛᴏ ᴛᴏᴘ ᴄᴏɴᴛʀɪʙᴜᴛᴏʀꜱ, ᴡᴇ'ʀᴇ ʜᴇʀᴇ ᴛᴏ ʀᴇᴄᴏɢɴɪᴢᴇ ᴇxᴄᴇʟʟᴇɴᴄᴇ.\n"
                "📊 Stay updated with real-time rankings, track your progress, and compete with friends to climb the leaderboard!\n"
                "❖Join us in celebrating achievements and fostering a vibrant community together!❖\n"
                "♡━━━━━━━━ ᴀʀɪ ━━━━━━━♡\n\n"
                "ᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ <a href=\"https://t.me/lll_notookk_lll\">||ᴀʀɪ||❣️</a>",
        reply_markup=keyboard
    )
    accha = await message.reply_text(
        text="__ᴅιиg ᴅιиg ꨄ︎ ѕтαятιиg..__"
    )
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅιиg ꨄ sтαятιиg.....__")
    await asyncio.sleep(0.2)
    await accha.edit("__ᴅιиg ᴅιиg ꨄ︎ sтαятιиg..__")
    await asyncio.sleep(0.2)
    await accha.delete()
