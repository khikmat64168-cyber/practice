"""Operators and Conditions 
    (1)Operators 
    (2)Conditions

    (3)Logical operators


    """

print("----OPERATORS----")
# + , - , < ,=< , > , is ,>=, * , ==,  /     // %  += **

a = 19
b = 5

# print("a > b", a > b)
# print("a / b", a / b)
# print("a * b", a * b)

print(a / b)
result = a // b
left = a % b
print(f"the result: {result} and left: {left}")


# a = a + 100
a += 100
print("a:", a)


print("b**2",  b**2)
print("b*b*b", b**3)

# print("=======")
print("="*5)


c = dict(name="Matt", age=25)
d = dict(name="Matt", age=25)
e = c
print("c==d", c == d)  # only value solishtirilinadi
print(id(c), id(d))


data = c is d
print("c is d ", c is d)
print("c is e ", c is e)
