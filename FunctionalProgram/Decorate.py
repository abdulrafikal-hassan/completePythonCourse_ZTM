# Decorators is programming Pattern 
# Decorators have the @ sign ff by the name
# Decorators super charge the ability of a function 
# Higher Order Function eihter accepts a func as a param or returns a param eg . map(),filter(), zip()

# creating my own decorator

def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('******')
    return wrap_func

@my_decorator
def hello():
    print('hellooo')

hello()

@my_decorator
def bye():
    print('GoodBye')

bye()

# this also works like the decorators but it is not advisable
# h2 = my_decorator(hello)()
# print(h2)


def new_decor(fun):
    def cover(*args, **kwargs):
        fun(*args, **kwargs)
    return cover

@new_decor
def say(greeting, emoji=':)'):
    print(greeting, emoji)

say('Hey ')

# Practical Applications of Decorators 
# building custom Decorators eg performance

from time import time 
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1} secs')
        return result 
    return wrapper

@performance
def long_time():
    for i in range(10000):
        i * 5

long_time()