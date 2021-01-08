# Date: 06.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: Ro'yxatlar bilan ishlash.

# 1. Har bir odamga alohida xabar yuboruvchi dastur 
ismlar=['Anvar','Islom','Lochin','Abdurasul','Ulug\'bek']
for ism in ismlar:
    print(f"Salom {ism}")
print(f"Kod {len(ismlar)} marta takrorlandi")

# 2. 10 dan 100 gacha bo'lgan toq sonlar kubini topish
toq_sonlar=list(range(11,100,2))
for son in toq_sonlar:
    print(f"{son} ning kubi {son**3} ga teng")

# 3. Yoqtirgan kinolar ro'yxatini chiqaruvchi dastur
kinolar=[]
print("Siz uchun sevimli bo'lgan 5 ta kinoni kiriting?")
for n in range(5):
    kinolar.append(input(f"{n+1}-kinoni kiriting? "))
print(f"Siz yoqtirgan kinolar ro'yxati: {kinolar}")

# 4. Suhbat qilgan odamlar ro'yxatini chiqaruvchi dastur
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)
