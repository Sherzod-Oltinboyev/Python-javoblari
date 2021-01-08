# Date: 04.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: String(Matn).
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati")

# Foydalanuvchi manzilini olish.
kocha=input("Ko'cha nomi?\n")
mahalla=input("Mahalla nomi?\n")
tuman=input("Tuman nomi?\n")
viloyat=input("Viloyat nomi?\n")
print(kocha.title()+" ko'chasi,\n"+mahalla.title()+" mahallasi,\n"+tuman.title()+" tumani,\n"+viloyat.title()+" viloyati")

# f-srting yordamida matn chiqarish
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
manzil=f"{kocha.title()} ko'chasi,{mahalla.upper()} mahallasi,{tuman.lower()} tumani,{viloyat.capitalize()} viloyati"
print(manzil)
