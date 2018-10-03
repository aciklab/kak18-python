#!/usr/bin/python3

import sqlite3
print(sqlite3.version)

baglanti = sqlite3.connect('veriler.db')

if(baglanti):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')

veritabani_sec = baglanti.cursor()

# veritabanı oluşturma
veritabani_sec.execute("""
CREATE TABLE kisiler(
kisiid INTEGER PRIMARY KEY,
kisino INTEGER NOT NULL ,
adi VARCHAR(50),
soyadi VARCHAR(50)
)
""")

# insert into
veritabani_sec.execute('''INSERT INTO kisiler (kisino,adi,soyadi) VALUES ('1234','Ali','Soyad')''')
baglanti.commit()
baglanti.close()

# select
oku = veritabani_sec.execute('SELECT * FROM kisiler')
print(oku.fetchall())
 
baglanti.commit()
baglanti.close()

# select2 
oku = veritabani_sec.execute('SELECT adi,soyadi,kisino from kisiler')
for verileri_cek in oku.fetchall():
    print('Adı Soyad : %s %s - Kişi NO : %s'%verileri_cek)
 
# fetchmany(istenen veri) : parantez içine yazılan satırdaki veriyi çeker.
# fetchone : ilk veriyi çeker.
baglanti.commit()
baglanti.close()

# row çekme
baglanti = sqlite3.connect('veriler.db')
baglanti.row_factory = sqlite3.Row
veritabani_sec = baglanti.cursor()
oku = veritabani_sec.execute('Select adi,soyadi,kisino from kisiler')
for verileri_cek in oku.fetchall():
    print(verileri_cek['adi'],verileri_cek['soyadi'],verileri_cek['kisino'])

baglanti.commit()
baglanti.close()

# veri silme
baglanti = sqlite3.connect('veriler.db')
baglanti.row_factory = sqlite3.Row

veritabani_sec.execute("DELETE from kisiler where adi='Serkan'")

oku = veritabani_sec.execute('Select adi,soyadi,kisino from kisiler')
for verileri_cek in oku.fetchall():
    print(verileri_cek['adi'],verileri_cek['soyadi'],verileri_cek['kisino'])
baglanti.commit()
baglanti.close()

# veri güncelleme
baglanti = sqlite3.connect('veriler.db')
baglanti.row_factory = sqlite3.Row

veritabani_sec = baglanti.cursor()
veritabani_sec.execute("update kisiler set adi='Ayşe' where adi='mehmet'")
oku = veritabani_sec.execute('Select adi,soyadi,kisino from kisiler')
for verileri_cek in oku.fetchall():
	print(verileri_cek['adi'],verileri_cek['soyadi'],verileri_cek['kisino'])
baglanti.commit()
baglanti.close()

# benzer veri bulma
baglanti = sqlite3.connect('veriler.db')
baglanti.row_factory = sqlite3.Row

veritabani_sec = baglanti.cursor()
oku = veritabani_sec.execute('SELECT * FROM kisiler Where adi LIKE "A%"') # A ile başlayan
for verileri_cek in oku.fetchall():
    print(verileri_cek['adi'])
baglanti.commit()
baglanti.close()

