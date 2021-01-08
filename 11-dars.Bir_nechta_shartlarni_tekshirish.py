# Date: 07.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: Bir nechta shartlarni tekshirish.

# 1. Juft yoki toqligini aniqlovchi dastur
j_son=int(input("Juft son kiriting? "))
if j_son%2==0 and j_son > 0:
    print("Raxmat!")
else:
    print("Bu son juft emas!")
    son=int(input("Boshqa son kiriting? "))
    if son%2==0 and son > 0:
        print("Raxmat")

# 2. Foydalanuvchidan yoshini so'ragan holda chipta narxini belgilash
yosh=int(input("Yoshingiz nechchida? "))
if yosh < 4 or yosh > 60:
    narx="bepul"
elif yosh < 18:
    narx=10000
else:
    narx=20000
print(f"Chipta narxi {narx}")

# 3. Sonlarni taqqoslash:
son1=float(input("Birinchi sonni kiriting: "))
son2=float(input("Ikkinchi sonni kiriting: "))
if son1==son2:
    print(f"{son1}={son2}")
elif son1 > son2:
    print(f"{son1}>{son2}")
else:
    print(f"{son1}<{son2}")

# 4.
mahsulotlar=['kartoshka','piyoz','sabzi','guruch','moy','un','mosh','karam','go\'sht','no\'xat']
savat=[]
print("Kamida 5 ta mahsulot nomini kiriting? ")
for n in range(5):
    savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))

if savat:
  for sav in savat:
      if sav in mahsulotlar:
          print(f"{sav.title()} do'konimizda bor")
      else:
          print(f"{sav.title()} do'konimizda yo'q")

else:
    print("Savatingiz bo'sh")
# 5.
mahsulotlar=['kartoshka','piyoz','sabzi','guruch','moy','un','mosh','karam','go\'sht','no\'xat']
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
print("Kamida 5 ta mahsulot nomini kiriting? ")
for n in range(5):
    savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for mahsulot in mavjud_emas:
       print(mahsulot.title())
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor!!!")

# 6. Loginni tekshirish

foydalanuvchilar=['anvar','lochin','islom','sherzod','oybek']
yangi=input("Yangi login tanlang: ")
if yangi.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz,{yangi.title()}")

# 7. Qoldiqni aniqlash

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
