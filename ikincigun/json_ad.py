#!/usr/bin/python

import json

class Person(object):
    def __init__(self, name, age,sehir):
        self.name = name
        self.age = age
        self.sehir = sehir
        
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)            

p1 = Person("Ali", 23,"ankara") 
p2 = Person("Veli", 29,"ankara")
p3 = Person("ornek", 29,"izmit")
p4 = Person("deneme", 29,"istanbul")
p5 = Person("ornek01", 29,"ankara")


people = []
people.append(json.loads(p1.toJson()))
people.append(json.loads(p2.toJson()))
people.append(json.loads(p3.toJson()))
people.append(json.loads(p4.toJson()))
people.append(json.loads(p5.toJson()))
json_data = json.dumps(people)

print(repr(json_data))
