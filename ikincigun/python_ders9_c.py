#!/usr/bin/python3

import re

patterns = [ "ali", "veli" , "cengiz"]
text = "ali, hasan, veli ve ahmet yolda geziyorlar"

for pattern in patterns:
	if re.search(pattern,  text):
		print("var!")
	else:
		print("yok")
