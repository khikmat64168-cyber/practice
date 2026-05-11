print("===============   Iterable Objects & Range   =================")


# Iterable objects : list , tuple , set , dict  , string ,range , map , filter

range_obj = range(3)
print("range_obj:", range_obj)


text = "MIT"
for letter in text:
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element : {ele}")


print("===============   Dictionary   =================")
# Dictionary is called as a JSON object

person = {"name": "Matt", "age": 25, "single": True}
person_obj = dict(name="Matt", age=25, single=True)
print(f"the person : {person}")
print(f"the person_obj : {person_obj}")


name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name} , hobby: {hobby} and balance: {balance}")


del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} => the value {person_obj[key]}")


# name = person_obj["hobby"]
# print ("name2:", name2)
