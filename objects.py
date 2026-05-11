''' OBJECTS 
     (1) What is the object
     (2) Iterable objects & Range
     (3) Dictionary
    (4)Error handling system 



'''

import array  # package /module
import math  # package /module
from math import ceil  # function

print("===============   What is the object  =================")
# an object has  state and method properties
# Everything is an object in Python


# classdan olingan instancelar

print(type('Hello world'))  # str classidan olingan object
print(type(100))  # int classidan olingan object
print(type(True))  # int classidan olingan object
print(type(array))  # int classidan olingan object
print(type(math))  # int classidan olingan object


# Paradigm > Functional programming > Object oriented programming
# OOP 4 concepts > Encapsulation , Abstraction , Inheritance , Polymorphism


result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)  # CALL
print("result2:", result2)


print("===============   Error handling system    =================")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:

    print("Passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)


except Exception as err:
    print("General Error:", err)


else:
    print("Executed successfully without any error")
finally:
    print("Final closiing logic")
