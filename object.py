# OOP
class PlayerCharacter:
    membership = True 
    # def __intit__(self,name)
    def __init__(self, name ='anonymous', age=0):
        # if (PlayerCharacter.membership):
        if (age > 18):
            self.name = name  # attributes
            self.age = age

    def shout(self):
        print(f'my nmae is {self.name}')
    def run(self, hello):
        print('run')
        print(f'this is my last class func {self.name}')


player1 = PlayerCharacter('cindy', 30)
player2 = PlayerCharacter('Messi', 20)

player1.attack = 'is diff'

print(player1.attack)

print(player1.run('Hey'))
print(player1.name)
print(player2.name)
print(player2.age)

