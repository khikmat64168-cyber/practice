'''CLASS DEEP DIVING
    (1)ENCAPSULATION
    (2)INHERITANCE
    (3)POLYMORPHISM
    (4)

'''

print("------ Inheritance-------")
# PARENT > CHILD
# PArent provides only public &   protected properties (state & METHOD) for children


class Animal:
    # state
    description = "The class is parent for animals "

    # constructor

    def __init__(self, voice):
        self.status = "This animal is alive "

        self.voice = voice

    # method

    def make_voice(self):
        print(f"The animal can make voice: {self.voice}")


class Dog(Animal):
  # state
  # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

  # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes , i can protect you !")


class Cat(Animal):  # child
  # state
  # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

  # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # child
  # state
  # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

  # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes i can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meow",  True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()


print("----------")

dog.make_voice()
cat.make_voice()


print("----------")
print(Animal.description)
print(Dog.description)


print(dog.voice)
print("dog.status:", dog.status)

print("cat.status:", cat.status)
