#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
data = {"name": "ÇVeliÇ", "age": 28}

print(data)

with open('insanlar.json', 'w') as f:
    json.dump(data, f)
