#!/usr/bin/python3


class HarfSay:
	def __init__(self):
		self.sesli_harfler = 'aeıioöuü'
		self.sayac = 0

	def kelime_sor(self):
		return input('Bir kelime girin: ')

	def seslidir(self, harf):
		return harf in self.sesli_harfler

	def artır(self):
		for harf in self.kelime:
			if self.seslidir(harf):
				self.sayac += 1
		return self.sayac

	def ekrana_bas(self):
		mesaj = "{} kelimesinde {} sesli harf var."
		sesli_harf_sayısı = self.artır()
		print(mesaj.format(self.kelime, sesli_harf_sayısı))

	def run(self):
		self.kelime = self.kelime_sor()
		self.ekrana_bas()

if __name__ == '__main__':
	sayac = HarfSay()
	sayac.run()



