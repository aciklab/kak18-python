#!/usr/bin/python3

import urllib.request
 
url=urllib.request
connection=url.urlopen('http://ali.orhun.net')
content=connection.read()
content=content.decode('utf-8')
print(content)
