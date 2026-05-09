print("=============== number =================")
# in Java , variable is a name of storage location 

# in python , variable is a name of reference 

count = 100
count_type = type(count)
print("count:" , count , count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()#method
result2 = count.numerator
print(result1, result2)


print("=============== string  =================")
#METHODS : upper() , lower () , title() , find(), replace()  


course = "AI  Python  Fullstack "
result = type(course) 
print(f"the result (1): {result} ")


result = course.title()
print(f"the result (2): {result}" )


result = course.upper() 
print(f"the result (3): {result}" )

result = course.replace("Fullstack" , " Masterclass") 
print(f"the result (4): {result}" )
print(course)
 
 
print("=============== boolean  =================")
 
#function > type() , input() , bool() , int() , str()

y = input("Give your value for y: ")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}" )



# TRUTHY vs FALSY values
#TRUTHY : True 100. -100  " Mit"
#FALSY : False 0 "" None

test_falsy = "" or False or 0 or None or 0

print("test_falsy:", bool(test_falsy))




test_truthy = "MIT" 

print(" test_truthy:", bool(test_truthy))
