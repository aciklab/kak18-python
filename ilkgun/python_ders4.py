#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################
###################################
#### Python Temel 2
###################################
###################################

import os, sys

###################################
#### 1. Karakterler
###################################

karakter1="a" * 3
print(karakter1)

karakter1="hay " * 2
print(karakter1)

for karakter in karakter1:
	print(karakter)

print(karakter1[2])
print(karakter1[0])
print(karakter1[-1])
print(karakter1[-2])

print(len(karakter1))

isminiz = input("İsminiz nedir?")

for i in range(len(isminiz)):
	print("İsminizin {}. harfi: {}".format(i, isminiz[i]))

print(karakter1[1:3])
print(karakter1[0:3])
print(karakter1[:3])
print(karakter1[1:-1])
print(karakter1[1:])



print(karakter1[::-1])

print(karakter1[0:4:2])

print(sorted("havelsan"))
#import locale
#sorted("çiçek", key=locale.strxfrm)

# ilk harfi değişrir
firma = "havelsan"
print("H"+firma[1:])

firma = "havelsan"
firma = "H"+firma[1:]
print(firma)


# sesli harf olayı
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler = ""
sessizler = ""
kelime = "deneme"
for i in kelime:
    if i in sesli_harfler:
        sesliler += i
    else:
        sessizler += i
print("sesli harfler: ", sesliler)
print("sessiz harfler: ", sessizler)


# replece metodu
veri0="merhaba"
veri1=veri0.replace("m", "M")
print(veri1)
veri1=veri0.replace("mer", "MER")
print(veri1)
veri1=veri0.replace("m", "")
print(veri1)


veri1=veri0.replace("a", "A")
print(veri1)
veri1=veri0.replace("a", "A",1)
print(veri1)

# split metodu
veri0="Kamu AçıkKaynak Konferansı"
veri1=veri0.split()
print(veri1)

veri0="Özgür Yazılım, Açık Kaynak, Bilgisayar"
veri1=veri0.split(", ")
print(veri1)

veri0="Özgür Yazılım, Açık Kaynak, Bilgisayar"
veri1=veri0.split(", ",1)
print(veri1)

print(veri0.split(", ")[0])
print(veri0.split(", ")[1])
print(veri0.split(", ")[2])

veri1=veri0.rsplit(", ",1)
print(veri1)

# splitlines metodu
veri0="""3. derste 5. deneme alt alta bir şeyler
yazmak gerekti sanki.
hem de "ilginç" şekilde
yazılar da yazabiliyoruz\n"""
print(veri0)

print(veri0.splitlines())
print(veri0.splitlines()[2])

print(veri0.splitlines(True))

# lower ve upper metodu
veri0="Kamu Açık Kaynak Konferansı"
veri1=veri0.lower()
print(veri1)

veri0="Kamu Açık Kaynak Konferansı"
veri2=veri0.upper()
print(veri2)

print(veri0.islower())
print(veri0.isupper())

print(veri1.islower())
print(veri2.islower())
print(veri2.isupper())

veri0="ornek12.pdf"
print(veri0.endswith(".pdf"))

veri0="ornek12.pdf"
print(veri0.startswith("ornek"))

# en uzun isim
isimler = ["ahmet", "mehmet", "hasan", "veli", "abdullah"]
print("en uzun:",max(isimler, key=len))
print("en kısa:",min(isimler, key=len))


###################################
#### 2. Sayılar
###################################

print(2*2)
print(3/2)


print(35+45)
print("35"+"45")

#print("35"+45)

# kaç bitlik yer kaplar

sayi1=5
sayi2=15
sayi3=22
floatsayi=3.5

print(sayi1.bit_length()) # 101
print(sayi2.bit_length()) # 1111
print(sayi3.bit_length()) # 10110
print((22).bit_length()) # 10110

# ratio
print(floatsayi)
print(floatsayi.as_integer_ratio())

# integer sorgu
print(floatsayi.is_integer())

# mutlak değer
print(abs(-2))

# bölüm ve kalan
orneksayi=sayi3/sayi1
print("bölen bölünen:",sayi3,sayi1)
print("örnekbölüm:",orneksayi)

print("bölüm ve kalan",divmod(sayi3,sayi1))
print("bölüm:",14 // 3)
print("kalan:",14 % 3)

# en büyük en küçük
sayilar=[32131, 32132, 43231, 75633, 42324, 12342]
print("en büyük:",max(sayilar))
print("en küçük:",min(sayilar))

# toplam
print("toplamı",sum(sayilar))
print("iki sayıyı listeli toplama",sum(sayilar,sayi1))


