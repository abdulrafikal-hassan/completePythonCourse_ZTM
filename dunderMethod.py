# Dunder methods are __builtinfunction__
# Dunder methods are special method names 

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age 
        self.my_dict = {
            'name': 'John',
            'isMarried': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __getitem__(self, i):
        return self.my_dict[i]
        
    def __call__(self):
        return('yess i am here ')


action_figure = Toy('red', 1)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure.__len__())
print(action_figure.__call__())
print(action_figure['isMarried'])
print(action_figure['name'])