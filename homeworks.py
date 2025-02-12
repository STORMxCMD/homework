juft_sonlar = 0
toq_sonlar = 0

while True:
    son = int(input("Musbat son kiriting 0 ni kiritisangiz dastur toxtaydi: "))
    
    if son == 0:
        print("Dastur toxtadi.")
        break
    elif son < 0:
        print("Musbat son kiriting")
    elif son % 2 == 0:
        juft_sonlar += 1
        print("juft son.")
    else:
        toq_sonlar += 1
        print("toq son.")


print(f"Juft sonlar soni: {juft_sonlar}")
print(f"Toq sonlar soni: {toq_sonlar}")

