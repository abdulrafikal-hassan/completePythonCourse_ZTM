# This allows you to inherit rom more than 1 class 

class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power 

    def attack(self):
        print(f'attacking with only {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name 
        self.arrows = arrows 

    def check_arrows(self):
        print(f'{self.arrows} left for attack')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 19)
print(hb1.attack())
print(hb1.check_arrows())
print(hb1.sign_in())

# MRO MEthod  Resolution Order uses depth first search algoritm

class X: num = 10
class Y(X): pass  
class Z(X): num = 1 

class M(Y,Z): pass 

print(M.__mro__)
print(M.num)
