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
