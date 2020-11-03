#Abstraction is hiding of info and only providing info that is needed

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age 

    def run(self):
        print(run)

    def speak(self):
        print(f'Am called {self._name} and am {self._age} of age.')

player1 = PlayerCharacter('Ama', 10)
print(player1.speak())

player1.name = '!!!'
player1.speak = 'Hellooo World'
print(player1.speak)

# Private variables are written as _name = 'john'
# Python has no true private values. or privacy 