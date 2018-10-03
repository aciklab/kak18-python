#!/usr/bin/python3
import random

#en basit
def temel():
	print("İlk Fonksiyon!")

temel()

# basit
def basitfonksiyon(isim, soyisim, şehir):
	print("-"*30)
	print("isim           : ", isim)
	print("soyisim        : ", soyisim)
	print("şehir          : ", şehir)
	print("-"*30)

basitfonksiyon("Ali", "Akkirman", "Ankara")
basitfonksiyon("Veli", "Kar", "Isparta")

# kare bul
def kare_bul(sayi):
	çıktı = "{} sayısının karesi {} sayısıdır"
	print(çıktı.format(sayi, sayi**2))

kare_bul(10)
kare_bul(121)
kare_bul(1312)


# rastgele sayı üretme fonksiyonu
def sayi_uret(ilk, son, adet):
	sayilar = set()
	while len(sayilar) < adet:
		sayilar.add(random.randrange(ilk, son))
	return sayilar

print(sayi_uret(0,100,6))
print(list(sayi_uret(0,100,6)))

# ismin ne
def ismin_ne():
    isim = input("İsminiz nedir? ")
    return isim

print("Merhaba {}".format(ismin_ne()))


