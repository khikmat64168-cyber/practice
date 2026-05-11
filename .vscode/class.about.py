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
Person.explain()
