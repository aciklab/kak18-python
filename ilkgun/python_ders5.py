#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################
###################################
#### Python Temel 3
###################################
###################################

import os, sys

###################################
#### 1. Listeler
###################################

# temel listeler
veri0="Özgür Yazılım, Açık Kaynak, Bilgisayar"
veri1=["Özgür Yazılım", "Açık Kaynak", "Bilgisayar"]

print(veri0)
print(veri1)

print(type(veri0))
print(type(veri1))

veri3 = ["Ali", "Veli", 67, 7.2]
print(veri3)
print(type(veri3))

print(veri3[0])
print(veri3[1])

# liste içerisinde liste (inception)
veri4 = ["Ali", ["Ankara", "İstanbul", "Elazığ"], 67, 7.2]
print(veri4)

print(veri4[0])
print(veri4[1])

# liste ve string farkı

boskarakter = ""
bosliste = []

print(veri0)
print(veri1)

print(veri0[0])
print(veri1[0])

print("string uzunluk",len(veri0))
print("liste madde sayısı",len(veri1))

# soru
print(len(veri0[0]))
print(len(veri1[0]))

# aralık belirtme
print(*range(2, 10))

# list fonksiyonu

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
print(alfabe.split())
print(alfabe.split("b"))
print(list(alfabe))

# liste elemanları
print(veri0)
print(veri0[0])
print(veri0[1])
print(veri0[-1])
print(veri0[0:1])

# çok boyutlu dizi
print("çok boyutlu:")
print(veri4)
print(veri4[1][2])

# replace dışında veri değiştirmek
veri1 = "kak17"
print(veri1)
veri1 = "K" + veri1[1:]
print(veri1)

print(veri4[0])
veri4[0] = "Veli"
print(veri4[0])


liste = [1, 2, 3]
liste[0:len(liste)] = 5, 6, 7
# liste[:] = 5, 6, 7
print(liste)

liste = liste + [8]
liste +=[9]
print(liste)

print(veri4)
print(liste)

print(veri4+liste)

# liste kopyalamak
listekopya1=liste
listekopya2 = liste[:]
listekopya3 = liste.copy()

# öğe silmek

print(liste)
del liste[0]
print("orijinal",liste,id(liste))
print("kopya1",listekopya1,id(listekopya1))
print("kopya2",listekopya2,id(listekopya2))


# tamamen silmek
#del liste

# liste üretmek:

liste1 = [i for i in range(100)]
liste2 = list(range(100))

liste3 = []
for i in range(100):
    liste2 += [i]

print(liste1)
print(liste2)
print(liste3)

# soru

liste1 = [i for i in range(100) if i % 2 == 0]

liste2 = []
for i in range(100):
    if i % 2 == 0:
        liste += [i]
    else:
		liste += 0


# append metodu
print(veri4)
veri4.append("test1")
print(veri4)
veri4.append(["bir","iki",3])

# extend metodu
print(veri4)
veri5=[1,2,"üç"]
veri4.extend(veri5)
print(veri4)

# insert metodu
print(veri4)
veri4.insert(0,"ali")
print(veri4)

# remove metodu
print(veri4)
veri4.remove("ali")
print(veri4)

print(veri4)
veri4.pop(0)
print(veri4)

# reverse
print(veri4)
print(veri4[::-1])
print(list(reversed(veri4[::-1])))
print(veri4)
veri4.reverse()
print(veri4)

# sort
veri5=[1,7,9,2,3,4]
print(veri5)
veri5.sort()
print(veri5)
veri5.sort(reverse=True)
print(veri5)

# index (indis numarası)
print(veri4.index("üç"))
print(veri4.index(1))

# count (verinin kaç kere geçtiği)
print(veri4.count(1))

###################################
#### 2. Demetler (değiştirilemez listeler)
###################################

demet = ("ahmet", "mehmet", 23, 67)
print("demet:",demet)
print(type(demet))

#liste
listedemet = ["ahmet", "mehmet", 23, 67]
print("liste:",listedemet)
print(type(listedemet))

demet2 = "ahmet", "mehmet", 23, 67
print("demet:",demet2)
print(type(demet2))

print(tuple('abcçdefgğhıijklmnoöprsştuüvyz'))

# tek öğreli demet:

demet3="ahmet",
print(demet3)


# index ve count metodu bulunmakta

###################################
#### 3. Sözlükler
###################################

kelimeler = {"kitap": "book", "bilgisayar": "computer"}
print(kelimeler)
print(type(kelimeler))

print(kelimeler["bilgisayar"])

kelimeler["insanlar"] = "people"
print(kelimeler["insanlar"])


# sözlük eklenen veri tipleri
test1 = (1,2)
kelimeler[test1] = "deneme1"
print(kelimeler)

test1 = 12
kelimeler[test1] = "deneme2"
print(kelimeler)

# değiştirme
kelimeler[12] = "deneme3"
print(kelimeler)

# sözlük üretme
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk1 = {i: harfler.index(i) for i in harfler}

# keys
print(kelimeler)
print(kelimeler.keys())
print(list(kelimeler.keys()))

# values
print(list(kelimeler.values()))

# get
degisken="kitap"
print(kelimeler.get(degisken))

# pop
print(kelimeler)
kelimeler.pop(12)
print(kelimeler)

# update

stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}

stok.update(yeni_stok)
print(stok)


###################################
#### 4. Kümeler
###################################

kume1=set()
print(type(kume1))

liste4=["elma", "armut", "kiraz"]
kume1 = set(liste4)
print(kume1)

string1="Kamu Açık Kaynak Konferansı"
kume2 = set(string1)
print(kume2)

liste = ["elma", "armut", "elma", "kiraz",
	"çilek", "kiraz", "elma", "kebap"]

for i in set(liste):
	print("{} listede {} kez geçiyor!".format(i, liste.count(i)))

# temizleme
print(kume1)
kume1.clear()
print(kume1)

# kopyala
print(kume2)
kume3=kume2.copy()
print(kume2)
print(kume3)

# ekle
kume1 = set(liste4)
print(kume1)
kume1.add("çilek")
print(kume1)
kume3 = set(liste4)

# fark
print(kume1)
print(kume3)

print(kume1.difference(kume3))
print(kume3.difference(kume1))

print(kume1-kume3)
print(kume3-kume1)

# öğe silme
print(kume3)
kume3.discard("elma") # hata almazsınız
#kume3.remove("elma") # hata alırsınız
print(kume3)

# kesişim
print(kume1)
print(kume3)
print(kume3.intersection(kume1))
print(kume3 & kume1)

print(kume1)
print(kume3)

# alt küme
print(kume3.issubset(kume1))
print(kume1.issubset(kume3))

# kapsar küme
print(kume3.issuperset(kume1))
print(kume1.issuperset(kume3))

# birleşim
print(kume1)
print(kume3)
print(kume3.union(kume1))
print(kume3 | kume1)

