# Date: 05.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: Sonlar.

# 1. Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son=input("Istalgan son kiriting:\n>>> ")
son=int(son)
print(str(son)+" ning kvadrati "+str(son**2)+" ga teng")
print(str(son)+" ning kubi "+str(son**3)+" ga teng")

# 2. Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini konsolga chiqaruvchi dastur
yosh=input("Yoshingiz nechchida?\n>>> ")
yosh=int(yosh)
t_yili=2021-yosh
print("Siz "+str(t_yili)+"-yilda tug'ilgansiz")

# 3. Foydalanuvchidan ikki son kiritishini so'rab,
# kiritilgan sonlarning yig'indisi,ayirmasi,ko'paytmasi va bo'linmasini chiqaruvchi dastur.
son1=int(input("Birinchi sonni kiriting: "))
son2=int(input("Ikkinchi sonni kiriting: "))
print("Yig'indisi="+str(son1+son2))
print("Ayirmasi="+str(son1-son2))
print("Ko'paytmasi="+str(son1*son2))
print("Bo'linmasi="+str(son1/son2))


