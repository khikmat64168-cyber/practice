''' LOOPS
    (1)for
    (2)break/ele

    (3) while

'''


print("----- for operatori------")
# Iterable objects > string, dict , tuple , list range map filter

text = "MIT"
nubms = [10, 7, 3, 4]
car_obj = dict(brand="Ferrari ",  year=2025)
range_obj = range

for letter in text:
    print(f"the letter: {letter}")


print("--------")

for number in nubms:
    print(f"the number: {number}")

print("----------")

for key in car_obj:
    print(f"the key:{key} => value: {car_obj.get(key)} ")


print("------------")

for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 100:
        print("Reached break")
        break
else:
    print("Looped successfully")


print("-------While operator -------")
numb = 40
while numb > 0:

    numb -= 10
    print(f" the numb equals {numb}")


print("------")

count = 0
while True:  # takrorlanish ketma ketligi aniq bo'gan hollarda ishlatamiz
    count += 1
    x = int(input("Find number"))

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print(f"Wrong , please find again23")
