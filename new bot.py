import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from sympy import sympify
import nest_asyncio  # Yangi kutubxona

# /start komandasi uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men kalkulyator botman. Matematik ifodani kiriting va men uni hisoblab beraman. Masalan: 2 + 2 * 3"
    )

# Matematik ifodani hisoblash uchun funksiya
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        expression = update.message.text
        result = sympify(expression)
        await update.message.reply_text(f"Natija: {result}")
    except Exception as e:
        await update.message.reply_text("Xato! Iltimos, to'g'ri matematik ifoda kiriting.")

# Asosiy funksiya
async def main():
    # Tokeningizni bu yerga joylashtiring
    BOT_TOKEN = "7785626519:AAEmCHgLjcGy4AkVEnFK5Mm1wCu8EVTy8BE"

    # Bot dasturini yaratish
    app = Application.builder().token(BOT_TOKEN).build()

    # Handlerlarni qo'shish
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    print("Bot ishga tushdi...")
    await app.run_polling()

# Dasturni ishga tushirish qismi
if __name__ == "__main__":
    # nest_asyncio yordamida mavjud asyncio tsiklini "yamash"
    nest_asyncio.apply()
    asyncio.run(main())
