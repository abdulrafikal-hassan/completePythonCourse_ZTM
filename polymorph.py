# Polymorphism == many forms 
# is the sharing of same method names but different functions

class User:
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')
    
    def walk(self):
        print('Do nothing')

class Human(User):
    def __init__(self, name, age,email):
        User.__init__(self, email)
        self.name = name
        self.age = age 

    def walk(self):
        User.walk(self)
        print(f'{self.name} is {self.age} of age is walking')

class Animal(User):
    def __init__(self, name, age,email):
        super().__init__(email)
        self.name = name 
        self.age = age 

    def walk(self):
        print(f'{self.name} is {self.age} of age, cant walk')

human = Human('John', 30, 'human@email.com')
animal = Animal('pussy', 2,'animal@email.com')

print(human.email)
print(animal.email)

# Does the samething (1)
print(human.walk())
print(animal.walk())

#Doess the samething (2)
def user_attack(char):
    char.walk()

user_attack(human)
# Does the samething (3)
for char in [human, animal]:
    char.walk()

#Introspection 
# This is the ability to determine the type of anoblect at runtime

print(dir(human))
print(dir(animal))

