#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request
 
url = "http://ali.orhun.net"
url_oku = urllib.request.urlopen(url)
soup = BeautifulSoup(url_oku, 'html.parser')
 
print(soup.title) 
print(soup.body) 
#print(soup.body.b) 
print(soup.a)
#print(soup.find_all('a',limit=1))
