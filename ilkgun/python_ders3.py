#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################
###################################
#### Python Temel 1 
###################################
###################################

import os, sys

###################################
#### 1. Merhaba Dünya
###################################

# Düz String
print("Merhaba Dünya")

# Değişken Kullanımı
veri1="Merhaba"
print(veri1)

# Karışık Örnekler
print(veri1+" Deneme 1")
print(veri1 + " Deneme 1")
print(veri1,"Deneme 1")

print("2. deneme "+veri1+" son\n")

print("3. deneme 'oldukça' güzel\n")

print("4. deneme \"oldukça\" ilginç\n")

print("""5. deneme alt alta bir şeyler
yazmak gerekti sanki.
hem de "ilginç" şekilde
yazılar da yazabiliyoruz\n""")

print("6. deneme\nalt alta bir şeyler\nyazmak")

# print parametreleri (sep ve end)
print(veri1,"Deneme 1")
print(veri1,"Deneme 1",sep="-")
print(veri1,"Deneme 1",sep=" - ")
print(veri1,"Deneme 1",sep=None)
print(veri1,"Deneme 1",sep="")

print("######### \n")

print(veri1,"Deneme 1",end=".")
print(veri1,"Deneme 2",end=".\n")
print(veri1,"Deneme 3",end=".\n")
print("deneme")

print("\n")

# yazıyı dosyaya yazdırma
print(veri1,"Deneme 1")

dosya1 = open("kak18_3p1.txt", "w")
print(veri1,"Deneme 1", file=dosya1)
dosya1.close()

dosya2 = open("kak18_3p2.txt", "w")
print(veri1,"Deneme 2", file=dosya2, flush=True)



dosya2.close()


dosya3 = open("kak18_3p3.txt", "w")
print(veri1,"Deneme 3", file=sys.stdout)
dosya3.close()

# len fonksiyonu
print(len(veri1))


###################################
#### 2. Kullanıcıdan Bilgi Almak
###################################

bilgi1="Ali"
print(bilgi1)

bilgi2=input()
print(bilgi2)

bilgi3=input("İsminiz Nedir?")
print(bilgi3)

print("Merhaba", bilgi3, "nasılsın?")

bilgi4=input("Kaç Yaşındasın?")
print("Yaşınız:",bilgi4)

# HATALI KOD
#print(bilgi4+1)
print("Yaşınızın 2 katının 1 eksiği:",int(bilgi4)*2-1)

###################################
#### 3. Veri tipleri ve dönüşümleri
###################################

print("İsim Girilen Değer:",type(bilgi3))
print("Yaş Girilen Değer:",type(bilgi4))

sayi1=input("1. sayı")
sayi2=input("2. sayı")

print("Sayı1:",type(sayi1))
print("Sayı2:",type(sayi2))

print("str toplama:",sayi1+sayi2)

sayi1_1=int(sayi1)
sayi2_1=int(sayi2)

print("Sayı1 yeni:",type(sayi1_1))
print("Sayı2 yeni:",type(sayi2_1))

print("int toplama:",sayi1_1+sayi2_1)

# float
print("1. sayı float:",float(sayi1_1))
print("1. string float:",float(sayi1))


# değişken içeriğini taşıma
bir=1
iki=2
uc=3

veri2=input("1 ile 3 arasında bir rakamı yazı ile giriniz.")
veri2_rakam=eval(veri2)
print(veri2_rakam)

# format
veri3="Ali"
veri4="Veli"
print(veri3+" ve "+veri4+" iyi bir arkadaş")
print("{} ve {} iyi bir arkadaş".format(veri3, veri4))

###################################
#### 4. Dosya Oluşturmak
###################################

###################################
#### 4.b Dosya Okumak
###################################

# Tüm İçeriği Ekrana Yazdırır
#dosya6 = open("kak18_dosya1.txt")
dosya6 = open("kak18_dosya1.txt","r")
print(dosya6.read())
dosya6.close()

# Alternatif
with open("kak18_dosya1.txt", "r") as dosya6:
	print(dosya6.read())

dosya6 = open("fihrist.txt")
print(fihrist.readlines())

# Satır satır çeker
dosya7 = open("kak18_dosya1.txt","r")
# 1. satır
print(dosya7.readline())
# 2. satır
print(dosya7.readline())
dosya7.close()

# Dosyayı tekrar okumak istersek:
dosya8 = open("kak18_dosya1.txt","r")
print(dosya7.readline())
print(dosya7.readline())
print(dosya7.readline())
dosya8.seek(10)
print(dosya7.readline())
print(dosya7.readline())
dosya8.tell()


###################################
#### 4.b Dosyaya yazı eklemek
###################################

# Tüm Dosyayı Silip Ekler
dosya4 = open("kak18_dosya1.txt", "w")
dosya4.write("Bir şeyler yazalım")
dosya4.close()

# Ekleme Yapar
dosya5 = open("kak18_dosya1.txt", "a")
dosya5.write("Bir şeyler ekleyelim.")
dosya5.close()

# Alternatif
with open("kak18_dosya1.txt", "a") as dosya5:
	dosya5.write("Bir şeyler ekleyelim.")

# Dosyanın başına bir şey eklemek
with open("kak18_dosya1.txt", "r+") as dosya5:
	veri = dosya5.read()
	dosya5.seek(0)
	dosya5.write("En başa ekleyelim, silmeden"+veri)





