#!/usr/bin/python

import json

with open('diskaynak.json') as f:
    config = json.load(f)
    print('İsim: {}'.format(config['isim']))
    print('Soyad: {}'.format(config['soyad']))
    print('Öğrenci: {}'.format(config['ogrenci']))
