import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8867250071:AAGnYWoI8rMbGxrqz2IedPcB75k7SIr9Ufk"
bot = telebot.TeleBot(BOT_TOKEN)

# আপনার চ্যানেল ও গ্রুপের ইউজারনেম (@ ছাড়া লিখবেন)
CHANNEL_USERNAME = "https://t.me/FactonAnime"  
GROUP_USERNAME = "https://t.me/FactonAnimeGroup"      
YOUTUBE_LINK = "https://youtube.com/@factonanime?si=91roef_sAfZPXWH-"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn_channel = InlineKeyboardButton("📢 Telegram Channel", url=f"https://t.me/{CHANNEL_USERNAME}")
    btn_group = InlineKeyboardButton("💬 Telegram Group", url=f"https://t.me/{GROUP_USERNAME}")
    btn_yt = InlineKeyboardButton("▶️ YouTube Channel", url=YOUTUBE_LINK)
    btn_check = InlineKeyboardButton("✅ Joined / Try Again", callback_data="check")
    
    markup.add(btn_channel)
    markup.add(btn_group)
    markup.add(btn_yt)
    markup.add(btn_check)
    
    bot.send_message(
        message.chat.id,
        "👋 **স্বাগতম!**\nভিডিওটি পেতে আগে আমাদের Telegram Channel, Group এবং YouTube Channel-এ সাবস্ক্রাইব করুন:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "check")
def check_sub(call):
    try:
        user_id = call.from_user.id
        ch_stat = bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id).status
        gp_stat = bot.get_chat_member(f"@{GROUP_USERNAME}", user_id).status

        if ch_stat in ['member', 'administrator', 'creator'] and gp_stat in ['member', 'administrator', 'creator']:
            bot.answer_callback_query(call.id, "✅ সাবস্ক্রিপশন সফল হয়েছে!")
            bot.send_message(call.message.chat.id, "🎉 এই নিন আপনার কার্টুন ভিডিও লিংক/ফাইল।")
        else:
            bot.answer_callback_query(call.id, "❌ আপনি সবগুলো চ্যানেলে জয়েন করেননি!", show_alert=True)
    except Exception as e:
        bot.answer_callback_query(call.id, "⚠️️ বটটিকে আপনার চ্যানেলে ও গ্রুপে Admin বানান!", show_alert=True)

print("Tenida Bot is Running...")
bot.infinity_polling()
