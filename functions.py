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


# DEFINE - build /qurish

def greet(a):
    # pass # bu yerda hech narsa bajarilmaydi , lekin sintaksis jihatdan qo'yish kerak
    print(f"How do you do , {a}")


def greeting(b):
    print("Greeting is executed")
    return f"Hi, {b}"


# CALL /execute - chaqirish / bajarish
result1 = greet('Matt')
print("result1:", result1)


result2 = greeting("John")
print("result2:", result2)
