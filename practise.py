# n = int(input())
# m = int(input())

# while n >= m:
#     n = n - m  

# qoldiq = n  
# print(qoldiq)



# n = int(input())
# m = 0

# while 2**m <= n:
#     m += 1

# print(m - 1)



# n = int(input())  
# summa = 0  
# raqamlar_soni = 0  

# while n > 0:
#     summa += n % 10  
#     raqamlar_soni += 1       
#     n //= 10         
# print("Raqamlar yig'indisi:", summa)
# print("Raqamlar soni:", raqamlar_soni)







import random

n = int(input())

taxmin = random.randint(1, 10)

if taxmin == n:
    print("Kompyuter topdi")
else:
    print("Kompyuter taxmin qildi, lekin bu noto'g'ri.")
