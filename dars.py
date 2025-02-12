# def pawn_check (x1, y1, x2, y2):
#     return x1==x2 and y2-y1==1

# print(pawn_check(2,3,2,3))

# # git init 
# # git remote add origin link 
# # git add .
# # git commit -m "words"
# # git push origin main 

# def rook_check(x1, y1, x2, y2):
#     return x1==x2 or y1==y2

# print(rook_check(1, 2, 8, 2))


# def knight_check(x1, y1, x2, y2):

#     ox=abs(x1-x2) 
#     oy=abs(y1-y2) 
    
#     return (ox==2 and oy==1) or (ox==1 and oy==2)

# print(knight_check(1,1,3,2))


# def king_check(x1,y1,x2,y2):
#     ox=abs(x1-x2)
#     oy=abs(y1-y2)

#     return(ox==1 and oy==1) or (ox==0 and oy==1) or (ox==1 and oy==0)

# print(king_check(2,1,2,2))


# class Person:
#     def __init__(self, first_name, last_name, year):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.year=year

#     def get_info(self):
#         print(f"Mening ismim {self.first_name}")
    
#     def get_age(self):
#         return 2025-self.year

# person1=Person("Asliddin", "Usmonov", 2008)
# person1.get_info() 
# print(person1.get_age)



class Pupil:
    def __init__(self,ism,fam,yil):
        self.ism=ism
        self.fam=fam
        self.yil=yil

class Manzil:
    def __init__(self,vil,tum,mfy,uy):
        self.vil=vil
        self.tum=tum
        self.mfy=mfy
        self.uy=uy 
        
        