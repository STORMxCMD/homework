import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import yt_dlp

# Bot Token (o'z tokeningizni kiriting)
BOT_TOKEN = "8051172311:AAHZL1KWzMZCbcrZAU0mWJeN--KYrTIK618"

# Videoni yuklab olish funksiyasi
async def download_video(url: str) -> str:
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': True,
    }

    loop = asyncio.get_event_loop()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=True))
        video_file = ydl.prepare_filename(info_dict)
    return video_file

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Menga YouTube yoki Instagram video havolasini yuboring. 😊"
    )

# Xabarlarni qayta ishlash funksiyasi
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    chat_id = update.effective_chat.id

    # URL tekshirish
    if "youtube.com" in message or "youtu.be" in message or "instagram.com" in message:
        await update.message.reply_text("Videoni yuklab olishni boshlayapman... ⏳")

        try:
            # Videoni yuklab olish
            video_file = await download_video(message)

            # Videoni Telegram orqali yuborish
            with open(video_file, "rb") as video:
                await context.bot.send_video(chat_id=chat_id, video=video, caption="Mana video! 🎥")

            # Yuklangan videoni o'chirish
            os.remove(video_file)

        except Exception as e:
            await update.message.reply_text(f"Xatolik yuz berdi: {str(e)}")
    else:
        await update.message.reply_text("Iltimos, to'g'ri video havolasini yuboring! 😊")

# Botni ishga tushirish
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Komandalar va handlerlarni ro'yxatdan o'tkazish
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi...")
    app.run_polling()
