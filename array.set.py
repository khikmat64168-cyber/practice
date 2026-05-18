'''Array & Get
(1)Array
(2)Set
(3)Specific Operators with set 
(4)

'''

from array import array
# unicode nima ?

print("========Array=======")
numbers = array("i", [1, 4, 5, 7, 8, 41])
print("numbers(1):", numbers)

numbers.append(100)

numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(5)
numbers.pop()
print("numbers(2):", numbers)


del numbers[0:2]
print("numbers(4):", numbers)


print("========Set=======")
# set of unique collecctiom without keeping order
new_numbers = array("i", [1, 4, 8, 1, 1, 5, 7, 8, 41])
numbs_set = set(new_numbers)

# print("numbs_set:", numbs_set)
print(f"the numbs_set: {numbs_set} and type: {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1):", numbs_set)


numbs_set.add(7)
print("numbs_set(2):", numbs_set)


print("========. Specific Operators with set :  =======")
# |  & - ^

a = {10, 20, 50}
b = {20, 40}
result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b   # difference

result4 = a ^ b   # symmetric difference

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
