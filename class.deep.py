'''CLASS DEEP DIVING
    (1)ENCAPSULATION
    (2)INHERITANCE
    (3)POLYMORPHISM
    (4)

'''

print("===============   ENCAPSULATION    =================")
'''
C++ , JAVA > public, priivate , protected
PHP Typescript > public , private , protected
Python > public __private. _protected

'''


class Account():
    # state
    description = "The class makes bank accounts "

    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)

        self.__amount -= amount

    @property  # decoratori setter ve getterlar
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("change ownership :", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change ownership :", new_owner)
        self.__owner = new_owner


my_account = Account("Matt", 1000)
my_account.get_balance()


print("--------")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()


print("---------")
my_account.amount = 1000000
my_account.owner = "Elon "
my_account.get_balance()


print("---------")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found :", err)


# getter vs setter
print("owner before change:", my_account.holder)  # state


# my_account.change_ownership("Ali")

my_account.holder = "Ali"  # setter

print("owner after :", my_account.holder)
