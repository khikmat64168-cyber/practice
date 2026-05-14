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


print("----OPERATORS----")
x = 15

if x > 50:
    print("Case A")

elif x > 10:
    print("Case B ")
else:
    print("Case C")


print("=======Logical OPerators =======")
age = 13
# age = 18
# person = None

# if age > 16:
# person = "Adult"
# else:
# person = "child"


# print("person:", person)


# Ternary

person = "adult " if age > 18 else " minor"
print("person:", person)


is_student = True
is_admin = False
is_guest = True
is_parent = False


if not is_student:
    print("Welcome here , do you want to be a student ")

elif is_admin:
    print("Please go to this office")

elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
