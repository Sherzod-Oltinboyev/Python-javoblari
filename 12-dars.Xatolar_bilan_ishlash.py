# Date: 08.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: Xatolar bilan ishlash.

# 1. Juft son eknligini tekshirish.

son = float(input("Juft son kiriting: "))
if son%2==0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")

# 2. Chipta narxini yoshga ko'ra belgilash

yosh = int((input("Yoshingiz nechida? ")))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

# 3. Sonlarni taqqoslash

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

# 4.a) Mahsulotlarni tekshirish

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat=[]

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")

# 4. b) Mahsulotlarni tekshirish

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo\'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
         print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 5. Loginni tekshirish

users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")

# 6. Qoldiqni aniqlash
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

