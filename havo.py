import requests
import json

# OpenWeatherMap API kalitini kiriting
api_key = "5f8a11fd97ef867dac5b1280f928804f"  # Bu yerga o'zingizning API kalitingizni kiriting

# Shahar nomini so'rash
city = input("Shahar nomini kiriting: ")

# Ob-havo ma'lumotlarini olish uchun URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=uz"

# HTTP so'rov yuborish
response = requests.get(url)

# Agar so'rov muvaffaqiyatli bo'lsa, ob-havo ma'lumotlarini chiqarish
if response.status_code == 200:
    data = response.json()

    # Ob-havo ma'lumotlari
    main_data = data["main"]
    weather_data = data["weather"][0]
    temperature = main_data["temp"]
    pressure = main_data["pressure"]
    humidity = main_data["humidity"]
    description = weather_data["description"]
    wind_speed = data["wind"]["speed"]

    print(f"\n{city} shahri bo'yicha ob-havo ma'lumotlari:")
    print(f"Harorat: {temperature}°C")
    print(f"Bosim: {pressure} hPa")
    print(f"Namlik: {humidity}%")
    print(f"Ob-havo: {description}")
    print(f"Shamol tezligi: {wind_speed} m/s")
    
    # Kelgusi kunlar ob-havo prognozi
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang=uz"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    print("\nKechagi va kelgusi kunlar ob-havo prognozi:")
    for forecast in forecast_data["list"]:
        dt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        description = forecast["weather"][0]["description"]
        print(f"{dt}: {temp}°C, {description}")
else:
    print("Shahar topilmadi yoki xatolik yuz berdi.")
