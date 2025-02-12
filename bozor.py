import telebot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

# TOKENingizni o'zgartiring
BOT_TOKEN = "7525031686:AAFDk2bKoglWmB7d4gJgXKFI0ZWpjW_TGgU"

# State uchun saqlash mexanizmi
state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

# Asosiy menyu klaviaturasi
def main_menu():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("Statistika", "E'lon qo'shish", "Mahsulotlarni qidirish")
    return markup

# Holatlar guruhi
class AdStates(StatesGroup):
    product_name = State()
    price = State()
    description = State()
    category = State()
    photo = State()

# Start komandasi
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, 
        "Assalomu alaykum! Virtual bozorga xush kelibsiz!",
        reply_markup=main_menu()
    )
    bot.delete_state(message.from_user.id, message.chat.id)

# E'lon qo'shish jarayonini boshlash
@bot.message_handler(func=lambda message: message.text == "E'lon qo'shish")
def add_ad_start(message):
    bot.send_message(message.chat.id, "Mahsulot nomini kiriting:")
    bot.set_state(message.from_user.id, AdStates.product_name, message.chat.id)

# Mahsulot nomi qabul qilish
@bot.message_handler(state=AdStates.product_name)
def process_product_name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['product_name'] = message.text
    bot.send_message(message.chat.id, "Mahsulot narxini kiriting (faqat raqam):")
    bot.set_state(message.from_user.id, AdStates.price, message.chat.id)

# Narxni qabul qilish
@bot.message_handler(state=AdStates.price)
def process_price(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Iltimos, narxni faqat raqam bilan kiriting.")
        return
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['price'] = message.text
    bot.send_message(message.chat.id, "Mahsulot tavsifini kiriting:")
    bot.set_state(message.from_user.id, AdStates.description, message.chat.id)

# Tavsifni qabul qilish
@bot.message_handler(state=AdStates.description)
def process_description(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['description'] = message.text
    bot.send_message(message.chat.id, "Mahsulot kategoriyasini kiriting:")
    bot.set_state(message.from_user.id, AdStates.category, message.chat.id)

# Kategoriya qabul qilish
@bot.message_handler(state=AdStates.category)
def process_category(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['category'] = message.text
    bot.send_message(message.chat.id, "Agar mahsulot rasmini yubormoqchi bo'lsangiz, yuboring. Aks holda 'Yo'q' deb yozing:")
    bot.set_state(message.from_user.id, AdStates.photo, message.chat.id)

# Rasmni yoki rasmsiz javobni qabul qilish
@bot.message_handler(state=AdStates.photo, content_types=['photo', 'text'])
def process_photo(message):
    photo = message.photo[-1].file_id if message.photo else None
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        # Ma'lumotlarni ekranga chiqaramiz (baza yoki faylga saqlash mumkin)
        ad_info = f"\u2705 *E'lon qo'shildi!*\n\n" \
                  f"\ud83d\udd8b *Nomi:* {data['product_name']}\n" \
                  f"\ud83d\udcb0 *Narxi:* {data['price']} so'm\n" \
                  f"\ud83d\udd04 *Tavsif:* {data['description']}\n" \
                  f"\ud83d\udcc1 *Kategoriya:* {data['category']}"
        
        bot.send_message(message.chat.id, ad_info, parse_mode="Markdown")
        if photo:
            bot.send_photo(message.chat.id, photo, caption="Rasm yuklandi \u2705")
        else:
            bot.send_message(message.chat.id, "Rasm yuborilmadi \u274c")

    bot.send_message(message.chat.id, "Asosiy menyuga qaytishingiz mumkin.", reply_markup=main_menu())
    bot.delete_state(message.from_user.id, message.chat.id)

# Jarayonni bekor qilish uchun komanda
@bot.message_handler(commands=["cancel"])
def cancel(message):
    bot.send_message(message.chat.id, "Jarayon bekor qilindi.", reply_markup=main_menu())
    bot.delete_state(message.from_user.id, message.chat.id)

# Noto'g'ri buyruq uchun handler
@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(
        message.chat.id, 
        "Noto'g'ri buyruq! Iltimos, menyudan birini tanlang.", 
        reply_markup=main_menu()
    )

# Botni ishga tushirish
if __name__ == "__main__":
    bot.infinity_polling()
