#Encapsulation is the binding of data and manipulating the data

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and am {self.age} years old')

player1 = PlayerCharacter('rafik', 20)
print(player1.speak())
print(player1.name)
