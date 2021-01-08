# Date: 06.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: Ro'yxatlar bilan ishlash.

# 1. Davlatlar ro'yxatini turli metodlardan foydalanib  konsolga chiqarish
davlatlar=['America','Fransiya','Turkiya','Germaniya','Malayziya']
print(davlatlar)
print("Davlatlar soni: ",len(davlatlar))
print("Alifbo tartibida tartiblangan ro'yxat: ",sorted(davlatlar))
print("Teskari alifbo tartibida tartiblangan ro'yxat: ",sorted(davlatlar, reverse=True))
print("Asl ro'yxat: ",davlatlar)
davlatlar.reverse()
print("Teskari tartiblangan asl ro'yxat: ",davlatlar)
davlatlar.sort()
print("Alifbo tartibida tartiblangan ro'yxat: ",davlatlar)
davlatlar.sort(reverse=True)
print('Teskari alifbo tartibida tartiblangan ro\'yxat: ',davlatlar)

# 2. Sonlar ro'yxatini turli usullarda konsolga chiqarish:

sonlar=list(range(120,1201,2))
sonlar4=[]
print("120 dan 1200 gacha juft sonlar ro'yxati: ",sonlar)
print("Yig'indisi=",sum(sonlar))
print("Eng katta va eng kichik son ayirmasi=",max(sonlar)-min(sonlar))
print("Ro'yxatdagi elemantlar soni=",len(sonlar))
print("Ro'yxat boshidan 20 ta son: ",sonlar[:21])
print("Ro'yxat o'rtasidan 20 ta son: ",sonlar[530:551])
print("Ro'yxat oxiridan 20 ta son: ",sonlar[-20:])
sonlar1=sonlar[:21]
sonlar2=sonlar[530:551]
sonlar3=sonlar[-20:]
sonlar4.append(sonlar1)
sonlar4.append(sonlar2)
sonlar4.append(sonlar3)
print("Ro'yxat boshidan, o'rtasidan, oxiridan 20 tadan olib tuzilgan yangi ro'yxat: ",sonlar4)

# 3. Nusxa olish va uni o'zgartirish

taomlar=['osh','manti','somsa','sho\'rva','shashlik']
nonushta=taomlar[:]
nonushta.pop(1)
nonushta.pop(3)
nonushta.append('sandvish')
nonushta.append('kofe')
print(taomlar)
print(nonushta)
nonushta=tuple(nonushta)
print(nonushta)


