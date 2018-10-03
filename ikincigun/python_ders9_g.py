#!/usr/bin/python3

import os
from bs4 import BeautifulSoup
import urllib.request

def searchTureng(word):
    url="http://www.tureng.com/search/"+word
    try:
        answer = urllib.request.urlopen(url)
    except:
        return "Bağlantı yok"
    soup = BeautifulSoup(answer, 'html.parser')
    trlated=''
    try:
        table = soup.find('table')
        td = table.findAll('td', attrs={'lang':'tr'})
        for val in td[0:5]:
            trlated = trlated + val.text + '\n'
        return trlated
    except:
        return "Bulunamadı !"

kelime="test"
sonuc = searchTureng(kelime)
print(sonuc)
