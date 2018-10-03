#!/usr/bin/python

import pymysql
db = pymysql.connect(host='192.168.59.3', port=3306, user='veli', passwd='1234', db='test1') 

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)


# create table
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS kisi")

sql = """CREATE TABLE kisi (
	isim  CHAR(20) NOT NULL,
	soyad  CHAR(20),
	yaş INT )"""

cursor.execute(sql)
db.close()

# insert 
cursor = db.cursor()

sql = """INSERT INTO kisi(isim,
	soyad, yas)
	VALUES ('Ali', 'Akkirman', 28)"""

cursor.execute(sql)
db.commit()
db.close()

# read

cursor = db.cursor()

sql = "SELECT * FROM kisi \
       WHERE yas > '%d'" % (20)
try:
	cursor.execute(sql)
	sonuclar = cursor.fetchall()
	for veri in sonuclar:
		isim = veri[0]
		soyad = veri[1]
		yas = veri[2]
		
		 print ("isim = %s,soyad = %s,yas = %d" % \
			(isim, soyad, yas ))
except:
	print ("Herhangi bir veriye ulaşılamadı")

db.close()

# update

cursor = db.cursor()

sql = "UPDATE kisi SET yas = yas + 1 \
	WHERE yas = '%d'" % (20)
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()

# delete

cursor = db.cursor()

sql = "DELETE FROM kisi WHERE yas > '%d'" % (25)
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()

db.close()
















