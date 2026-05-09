''' FUNCTIONS 
  (1) DEFINE vs CALL
  (2) Parameters vs Arguments
  (3) Keyword & default arguments
  (4) Scope 
  
  
'''

print("===============   DEFINE vs CALL  =================")

# buildin functions > print() ,type(). - bizlar uchun yasab berilgan

# Function - reusable block of code -- malum mantiqni ishga tushuradigan codeblock
# Instead of block { } in JAVA  , Python uses indentation to define ({} ning o'rniga)


# DEFINE - build /qurish. parametr

def greet(a):
    # pass # bu yerda hech narsa bajarilmaydi , lekin sintaksis jihatdan qo'yish kerak
    print(f"How do you do , {a}")


def greeting(b):
    print("Greeting is executed")
    return f"Hi, {b}"


# CALL /execute - chaqirish / bajarish.  argument
result1 = greet('Matt')
print("result1:", result1)


result2 = greeting("John")
print("result2:", result2)


print("===============   Keyword & default arguments  =================")
# oqilishgina oson bo'lishi uchun
# DEFINE


def give_greet(name, age=30):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL


result3 = give_greet(name="Matthew", age=30)
print("result3:", result3)


result4 = give_greet("Jack")
print("result4:", result4)


print("===============   Scope  =================")
# scope larda priority tushunchasi mavjud.
b = 100


def calculate(a, b):
    c = a * b
    print(f"the c value: {c}")


# CALL
calculate(5, 50)
