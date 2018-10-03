#!/usr/bin/python3

import sys, os, datetime

sayı = input('Bir sayı girin: ')
if int(sayı) < 0:
	print('çıkılıyor...')
	sys.exit()
else:
	print(sayı)


# argüman alabilir

print(len(sys.argv))
print(sys.argv)

# versiyon

print(sys.version)

# bulunulan dizin
print(os.getcwd())
# cd alternatifi
os.chdir('../')
print(os.getcwd())
# ls alternatifi
print(os.listdir())

print(os.listdir(os.curdir))
print(os.listdir(os.pardir))

os.chdir('gün2')
#os.mkdir('yenidizin')
#os.makedirs('aylar/mayıs/ödeme/')

#os.remove("a.txt")
#os.rmdir("denemeklasor")

#os.system("python a.py")

# klasör ve dosya var mı?
os.path.isdir('/home/alorak')
os.path.isfile('/home/alorak/ali.txt')

os.path.split('/home/alorak/Desktop') # son klasörü ayırır

# dosya ve uzantısını ayırır
deneme="a.txt"
dosya, uzantı = os.path.splitext(deneme)


# datetime

suan=datetime.datetime.now()

suan.month #ay
suan.day #gün
suan.hour #saat
suan.minute #dakika
suan.second #saniye
suan.microsecond #mikrosaniye


suan = datetime.datetime.now()
tarih = datetime.datetime.ctime(suan)
print(tarih)

print(datetime.datetime.strftime(suan, '%A'))
print(datetime.datetime.strftime(suan, '%d %B %Y'))

tarih = datetime.datetime.now()
zaman_damgasi = datetime.datetime.timestamp(tarih)
print(zaman_damgasi)
tarih = datetime.datetime.fromtimestamp(zaman_damgasi)
print(tarih)


# kaç gündür hayattayım
bugün = datetime.datetime.today()
doğumgünü = datetime.datetime(1989, 9, 9)
fark = bugün - doğumgünü
print(fark)


# 200 gün gerisi
bugün = datetime.datetime.today()
fark = datetime.timedelta(days=200)
geçmiş = bugün - fark
print(geçmiş)

print(geçmiş.strftime('%c'))



