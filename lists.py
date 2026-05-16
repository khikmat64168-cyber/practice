''' Lists
   (1) Working  with lists
   (2)List methods
   (3)lambda function
   (4)enumarate , map , filter


'''

print("---  Working  with lists ---")
# Java/pHP/ NodeJs array = > Python list


# literal
person = {"name": "Matt", "age": "25"}  # dictinory
people = {"Andrew", "John", "Matt"}  # tuple
groups = {"MIT", "FLEXY", "DEVEX", "MG"}  # list
for team in groups:
    print(f"the team: {team}")


# constructor    bu classlar orqali degani

letters = list("Hello world!")
print(f"the letters: {letters} and size {len(letters)}")

print("-------")
fruits = ["apple", "orange", "lemon", "kiwi"]


a = fruits[0]
b = fruits[0:2]  # [0;2) yarim interval
c = fruits[::3]
d = fruits[:: -1]  # . teskari qlish uchun


print("a:", a)
print("b:", b)
print("c:", c)
print("d: ", d)


print("---  Lists methods  ---")
# methods > append() , insert(), pop() , remove(), clear() , sort(), index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append result: {letters}")


letters.insert(0,  "z")  # add front
print(f"the insert result: {letters}")


size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")


result2 = letters.pop(0)  # pop front
print(f"the pop result2: {result2} and letters: {letters}")


print("-------")

animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete  :", animals)


exist = animals.index("cat")
print("cat exist:", exist)


animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("indec of cat: ", animals.index("cat"))
else:
    print("cat does not exist  ")


print("-------")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sort default :", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)


# immutable >. sorted function & index()methods
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


print("---  Lambda functions  ---")
# lamda is small anonymous function !


def calculate(x, y): return x * y


result = calculate(3, 5)
print("results:", result)


people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40),
]

people.sort()
print("people1", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people2:", people)


print("--- enumerate , map , filter  ---")


# enumerate (index va valuelarning qiymatini bir vaqtda qabul qilinishi uchun ishlatilinadi  ) for index & value

animals = ["dog", "cat"]
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"the indec: {index} and value: {value} ")


# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)
result = car_obj.items()
# print("result:", result )
for (key, value) in result:
    print(f"the key: {key} and value: {value}")


print("-------")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)


]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_car:", new_cars)


result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
# print(f"the result1: {result1} and type : {type(result_map)}")


new_cars = list(result_map)
print("new_cars(2)", new_cars)


print("-------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result _filter: {result_filter} and type : {type(result_filter)}")
print(list(result_filter))
