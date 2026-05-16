'''Tuple
   (1)What is tuple: typle vs list
   (2)Unpacking arguments 
   (3)zip
   


'''


print("------ What is tuple: typle vs list ----- ")
# Java/pHP/ NodeJs array = > Python list

# literal

numbs = [3, 5, 1, 2]
print(numbs)
# car_dict = {"brand": "Ferrari", "year": 1995}

# constructor

letters = list("Hello World")
# person_dict = dict(name="Matt", age=35)
print(letters)


fruits = ["apple", " lemon", "kiwi", "banana"]

print("before fruits:", fruits)


fruits[2] = "melon"
print("after fruits :", fruits)

# we can not mutate tuple
animals = ("dog", "cat", "fish", "lion ")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"

# try avoid this
people = "Andrew", "John"
animals = "dogs"


print("------ Unpacking arguments  ----- ")
groups = ["MIt", "Flexy", "DEVEX", "Mg"]
(x, y, *z) = groups
print(f"the x : {x} and y: {y}")
print("z:", z)  # list


# . *args > tuple


def calculate(*args):
    total = 1
    for x in args:
        total *= x
    print(f"the type(args) value: {type(args)}")
    print(f"the total value: {total}")
    return total


calculate(1, 7, 2, 3)


print("------ ")
calculate(0, 2, 300)

print("------ ")
calculate(5, 7)

# **kwargs. dictinory lar orqali hosil bo'lishi


def introduce(**kwargs):
    print(f"the type(**kwargs) value:{type(kwargs)}")
    print(f"Hi i am {kwargs['name']} and i am {kwargs['age']} years old ")

    pass

# CALL


# def give_greet(name, age=22):
 #   print("give_great is executed")
  #  return f"Hi {name}, you are {age} years old "

introduce(name="Justin", age=28)
introduce(name="Matt", age=25, single=True)


def greeting(*args, **kwargs):
    print("*args > ", args)
    print("**kwargs >", kwargs)


greeting(
    "hi", True, 10,  # shu yergacha tuple ko'rinishida qabul qildirtiradi
    name="Matt ", age=20  # shu yergacha kwargsga dictionary ko'rinishida qabul qildirtiradi
)
