# Inheritance take the properties of other classes 

# Users can have multiple forms and is done by using inheritance 
class User:
# has no __init__ bcos it has no variables or values
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attcking with {self.num_arrows} number of arrows left')

class Ogres(User):
    def __init__(self, name, num):
        self.name = name 
        self.num = num 

    def attack(self):
        print(f'attacking with from {self.name} with {self.num} left')

wizard1 = Wizard('Merlin', 50)
archer = Archer('Robbin', 1000)
oger = Ogres('OrgerKing', 50)

print(wizard1.attack())
print(archer.attack())
print(oger.attack())

# Checking if something is an instance 

print(isinstance(wizard1, User))
print(isinstance(oger, object))