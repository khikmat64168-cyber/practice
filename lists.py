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
