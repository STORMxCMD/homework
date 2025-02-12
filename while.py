# i=int(input())

# while i<10 :
#     i=i+1
#     if i%2 :
#         continue
#     print(i)


# i=int(input())

# while i<10 :
#     i=i+1
#     if i%2==0 :
#         continue 
#     print(i)

# n = int(input("n = "))

# i = 0
# summa = 0

# while i < n:
#     i += 1
#     summa += i

# print(summa)



# n = int(input("n = "))

# i = 0
# summa = 0

# while i < n:
#     i += 1
#     if i % 2 == 0:  
#         summa += i

# print(summa)


# n=int(input())

# summa = 0

# while n > 0:
#     summa += n % 10  
#     n //= 10

# print(summa)


n = int(input())
kopaytma = 1
i = 1

while i <= n:
    kopaytma *= i  
    i += 1  
print(kopaytma)






import random

# Foydalanuvchidan son so'rash
son = int(input("1 dan 10 gacha bo'lgan sonni kiriting: "))

# Tasodifiy son generatsiya qilish
tasodifiy_son = random.randint(1, 10)

# Yigirma marta urinish imkoniyati
urinishlar_soni = 0

while urinishlar_soni < 20:
    urinishlar_soni += 1
    print(f"\nUrinish {urinishlar_soni}:")
    
    # Foydalanuvchidan yangi tahmin olish
    tahmin = int(input("Tahminingizni kiriting: "))
    
    if tahmin < tasodifiy_son:
        print("Sizning tahminingiz kichik.")
    elif tahmin > tasodifiy_son:
        print("Sizning tahminingiz katta.")
    else:
        print(f"Tabriklayman! Siz {urinishlar_soni}-chi urinishda to'g'ri topdingiz!")
        break

if urinishlar_soni == 20:
    print(f"\nAfsuski, 20 urinishdan so'ng ham to'g'ri topa olmadingiz. Tasodifiy son {tasodifiy_son} edi.")

