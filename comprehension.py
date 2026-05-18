'''Comprehension.   # boshqa tildagi spread operator bilan bir hil
 (1)What is comprehension & List comp.
 (2)set and dictionary comp 
'''


print("==== What is comprehension & List comp.  ===== ")
# comprehension act like sprad operator


'''Comprehension  general syntax kop uchraydigan formalar
   (a) * iterable 
   (b) < expression >  for item in iterable 
   (c) < expression > for item in iterable < condition >


'''

# list comp.

numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version
print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

people = [("Robert", 22), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]  # b version

print("list_people:", list_people)

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)

]

list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)


print("==== set and dictionary comp   ===== ")
numbs = [1, 4, 5, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)


dict_people = {person[0]: person[1] for person in people}
print("dict_people:", dict_people)


dict_people2 = {person[0]: person[1] for person in people if person[1] > 20}
print("dict_people2:", dict_people2)
