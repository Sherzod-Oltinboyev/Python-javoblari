# Date: 05.01.2021.
# Author: Sherzod Oltinbpoyev.
# Theme: List(Ro'yxat).

ismlar=['Anvar',"Islom",'Ilhom']
print("Salom "+ismlar[0]+","+"Ahvollaring yaxshimi?")
print(ismlar[1]+",ertaga darsga borasanmi?")
print(ismlar[2]+" ishlaringga omad!!!")

# 2. List ichidagi sonlar ustida turli arifmetik amallar bajarish.

sonlar=[13,54,-54,1200,54.7,-6.8]
summa=sonlar[3]+sonlar[5]
ayirma=sonlar[0]-300
kopaytma=sonlar[-1]*sonlar[0]
sonlar[2]=1000
print(summa)
print(ayirma)
print(kopaytma)
print(sonlar)

# 3. List ichidan elementlarni olish va joylash

t_shaxslar=['Amir Temur',"Alisher Navoiy",'Steve Jobs']
z_shaxslar=['Bill Geyts','Bobir Aqilxonov ','Zakir Naky']
tarixiy=t_shaxslar.pop(0)
zamonaviy=z_shaxslar.pop(2)
print("Men tarixiy shaxslardan "+tarixiy+" bilan,\nzamonaviy shaxslardan esa "
      +zamonaviy+" bilan\n suhbat qilishni istar edim.")

# 4. Mehmonlar ro'yxati

friends=[]
friends.append('Islom')
friends.append('Oybek')
friends.append("Ixtiyor")
friends.append("Sardor")
friends.append("Akbar")
friends.remove("Akbar")
friends.remove("Islom")
friends.insert(0,"Ilhom")
friends.insert(3,"Odil")
friends.append("Muhammad")
print(friends)

# 5. pop() va append() metodlari yordamida yangi list hosil qilish

mehmonlar=[]
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop())
print("Kelgan mexmonlar ro'yxati: ",mehmonlar)
