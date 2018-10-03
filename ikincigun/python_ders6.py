#!/usr/bin/python3
# -*- coding: utf-8 -*-

###################################
###################################
#### Python Temel 4
###################################
###################################

import os, sys

###################################
#### 1. İşleçler
###################################

print(7+3)
print(7*3)
print(7-3)
print(7/3)

# kuvvet
print(7**3)
print(pow(7,3))

# kalan
print(7%3)

# bölüm
print(7//3)

sayi1=2.55
sayi2=2.12
print("round:",round(sayi1))
print("integer:",int(sayi1))

print("round2:",round(sayi2))
print("integer2:",int(sayi2))

# karşılaştırma

if "1" == "1":
	print("bir bire eşittir!")
else:
	print("saçma bir dünyadasın!")

# büyüklük küçüklük ile ilgili
print(sayi1)

if int(sayi1) <= 2:
	print("sayı 2 veya 2'den küçük")
else:
	print("sayı 2'den büyük")

## ==	eşittir
## !=	eşit değildir
## >	büyüktür
## <	küçüktür
## >=	büyük eşittir
## <=	küçük eşittir

# bool mantığı

a = "gdfg"
print(bool(a))
a = ""
print(bool(a))

a = 0
print(bool(a))

a = 12
print(bool(a))

print(bool(a==1))
print(bool(1==1))

if 1==1 == True:
	print("Yaşasın Bilim!")

if 1==1 and 2**2==4 == True: # ve var
	print("Doğru")

if 1==1 or 2**2==5 == True: # veya var
	print("Doğru")

if not 1==1:
	print("Yanlış")
else:
	print("Doğru")

# kısayollar

a = 20
print(a)
a += 2
print(a)

a = 20
print(a)
a *= 2
print(a)

a = 20
print(a)
a -= 2
print(a)

a = 21
print(a)
a %= 2
print(a)

a = 21
print(a)
a **= 2
print(a)

# aitlik
degisken = "ali"
print("a" in degisken)

# kimlik

degisken=1000
print(id(1000))
print(id(degisken))
print(id("degisken"))

print(degisken is 1000)

###################################
#### 2. Döngüler
###################################


# IF

# Döngü örneği
sayi1=12
#tahmin=input()
tahmin=1
print(tahmin)
print(sayi1)

if int(tahmin) == sayi1:
    print("Tebrikler!")
else:
    print("Ne yazık ki tuttuğum sayı bu değildi...")


deger1=1
if int(deger1) == 1:
    print("bir")
elif int(deger1) == 2:
	print("iki")
elif int(deger1) == 3:
	print("üç")
else:
    print("diğer")



# WHILE
a = 1
while a < 10:
	a +=1
	print(a,". değer")

a = 1
while a < 10:
	print(a,". değer")
	a +=1

while True:
	soru = input("Nasılsınız, iyi misiniz?")
	if soru == "q":
		break 

while True:
    parola = input("parola belirleyin: ")
    elif len(parola) in range(3, 8):
        print("Yeni parolanız", parola)
        break
    else:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

# FOR

tr_harfler = "şçöğüİı"
for harf in tr_harfler:
	print(harf)

for i in range(0, 10):
	print(i)

for i in range(3):
	print(i)

for i in range(0, 10, 2):
	print(i)

for i in range(10, 0, -1):
	print(i)














