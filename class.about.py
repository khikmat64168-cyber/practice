'''CLASS
    (1)what is the class
    (2)Ordinary vs static properties
    (3) special methods


'''
print("===============   What is the class  =================")
# class - blueprint for creating objects
# structure > state structor method


class Person():
    # state
    message = "class state properties"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"the{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age} !")

    @classmethod
    def explain_class(cls):
        print(f"static method property is executed")


person1 = Person("Matt", 25)
person2 = Person("John", 30)
person3 = Person("Jack", 35)


# ordinary state
print("person1 name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print("===============   Ordinary vs static properties  =================")
new_messsage = Person.message
print("new_message:", new_messsage)

# static method
Person.explain_class()


print("===============   Special/ Magic methods  =================")

# python's most common special methods are below
# __init__() - constructor method
# __str__() - string representation of the object
# __new__() - object creation method
# __call__() - callable objects
# __len__() - length of the object
# __eq__() - equality comparison
# __getirtem__() - attribute access


class Car():
    # state
    description = "This  class makes cars"
    # constructor

    def __new__(cls, *args):
        print("* __new__ *")
        return super().__new__(cls)

    def __init__(self,  year, name):
        self.name = name
        self.year = year
    # method

    def start_engine(self):
        print(f"{self.name} started engine ")

    def stop_engine(self):
        print(f"{self.name} stopped engine ")

    def __str__(self):
        return f"the car.name : {self.name} was produced in  {self.year} year!"

    def __call__(self):
        print("object is called as a function")
        return True


my_car = Car(2026, "Ferrari")

my_car.start_engine()
my_car.stop_engine()

print("----")
your_car = Car(2025, "Lamborghini")
print(your_car)
response = your_car()
print("response:", response)
