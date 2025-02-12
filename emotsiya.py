import telebot
import requests

# Bot tokenini o'zgaruvchiga saqlash
TOKEN = '8165977721:AAGF8myOxbPgLZP5vq4A2pBAUZJkPOLY_so'
API_KEY = '235a911a'
BASE_URL = "http://www.omdbapi.com/"

bot = telebot.TeleBot(TOKEN)

# Kino janrlari
movies = {
    "Action": [
        "Mad Max: Fury Road",
        "Die Hard",
        "John Wick",
        "Avengers: Endgame",
        "The Dark Knight",
        "Terminator 2"
    ],
    "Comedy": [
        "The Hangover",
        "Superbad",
        "Step Brothers",
        "Anchorman",
        "The Big Lebowski"
    ],
    "Drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "The Godfather",
        "The Pursuit of Happyness",
        "Gladiator"
    ],
    "Horror": [
        "The Conjuring",
        "It",
        "A Nightmare on Elm Street",
        "Get Out",
        "Hereditary"
    ]
}

# Kino tavsiyalari menyusi
@bot.message_handler(commands=['recommend'])
def recommend(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("Action"), telebot.types.KeyboardButton("Comedy"),
               telebot.types.KeyboardButton("Drama"), telebot.types.KeyboardButton("Horror"))
    bot.send_message(message.chat.id, "Kinolar janrlarini tanlang:", reply_markup=markup)

# Kino janrini tanlash
@bot.message_handler(func=lambda message: message.text in movies.keys())
def handle_genre(message):
    genre = message.text
    movie_list = movies.get(genre, [])
    if not movie_list:
        bot.send_message(message.chat.id, f"Bu janrda kino mavjud emas.")
        return

    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    for movie in movie_list:
        markup.add(telebot.types.KeyboardButton(movie))

    bot.send_message(message.chat.id, f"Mana sizga ba'zi {genre} janridagi kinolarni tanlang:", reply_markup=markup)

# Filmni tanlash
@bot.message_handler(func=lambda message: any(movie in message.text for genre in movies.values() for movie in genre))
def handle_movie(message):
    movie_name = message.text
    url = f"{BASE_URL}?t={movie_name}&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        bot.send_message(message.chat.id, f"Xatolik: API so'rovi amalga oshirilmadi. Status kodi: {response.status_code}")
        return

    try:
        movie = response.json()
    except requests.exceptions.JSONDecodeError:
        bot.send_message(message.chat.id, "Xatolik: API javobi noto'g'ri formatda.")
        return

    if movie.get("Response") == "False":
        bot.send_message(message.chat.id, f"'{movie_name}' nomli film topilmadi.")
        return

    title = movie.get("Title", "Noma'lum")
    year = movie.get("Year", "Noma'lum")
    plot = movie.get("Plot", "Ma'lumot mavjud emas.")
    imdb_rating = movie.get("imdbRating", "N/A")
    poster_url = movie.get("Poster", "")

    response_message = f"Film: {title} ({year})\nIMDB reytingi: {imdb_rating}\n\n{plot}"

    if poster_url:
        bot.send_photo(message.chat.id, poster_url, caption=response_message)
    else:
        bot.send_message(message.chat.id, response_message)

    # Filmni yuklash linkini yuborish (hozirgi kunda yuklashni amalga oshirishni faqat omdbAPI orqali qilish qiyin)
    # Shuning uchun, mana shunday xabar yuboramiz:
    bot.send_message(message.chat.id, f"Filmni yuklab olish uchun quyidagi havolani sinab ko'ring:\n"
                                      f"Yuklab olish: [Film yuklash havolasi]")

# Boshlang'ich buyruq
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom! Kino botiga xush kelibsiz.\n\n"
        "Kinolarni tavsiya qilish uchun /recommend buyrug'ini yuboring.\n"
        "Yoki ma'lum bir filmni qidirish uchun /search <film nomi> buyrug'ini yuboring."
    )

# Botni ishga tushirish
if __name__ == "__main__":
    bot.polling(none_stop=True)
