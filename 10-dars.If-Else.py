# Date: 07.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: If-Else.

# 1. Mashina nomlarini upper() va title() metodlari va shart orqali konsolga chiqarish
yangi=['toyota','mazda','hyundai','gm','kia']
for yan in yangi:
    if yan=='gm':
        print(yan.upper())
    else:
        print(yan.title())

# 2. != teng emas sharti orqali konsolga chiqarish
yangi=['toyota','mazda','hyundai','gm','kia']
for yan in yangi:
    if yan!='gm':
        print(yan.title())
    else:
        print(yan.upper())
# 3. Foydalanuvchidan login ismini sorash orqali boshqa loginlar bilan solishhtirish
login=input("Login ismingizni kiriting? ")
login=login.title()
if login.lower()=="admin":
    print(f"Xush kelibsiz,{login} Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz,{login}!")

# 4. Sonlarni taqqoslash
son1=int(input("Birinchi sonni kiriting? "))
son2=int(input("Ikkinchi sonni kiriting? "))
if son1==son2:
    print("Sonlar teng")

# 5. Sonlarni manfiy yoki musbat ekanligini tekshirish
son=int(input("Istalgan sonni kiriting? "))
if son > 0:
    print("Musbat son")
else:
    print("Manfiy son")

# 6.
son3=int(input("Istalgan sonni kiriting biz uni ildizini topib beramiz? "))
if son3 > 0:
    print(son3**(1/2))
if son3 < 0:
    musbat=int(input("Musbat sonni kiriting, manfiy sonni ildizi yo'q? "))
    print(musbat**(1/2))
