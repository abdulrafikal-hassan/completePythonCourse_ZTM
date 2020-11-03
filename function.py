#Functions are created with the def key word  and allow us DRY
#Functions should do 1 thing really well
# Should return something 
def say_hello():
    print('hellooooo')

say_hello()

# Positional Arguments 
def greet(name, message):
    print(f'Hello {name} have a good day, and you said this {message}')

#Positional Parameters 
greet('Rafik','Do whatever it is to be good')
greet('Adrei','Thanks for a Great Course')
 
#Keyword Arguments
greet(message='What a nice Day', name='Neagoie')

#Default parameters
def say_Name(name='John Doe',age=20):
    print(f'Your are {name} and {age} years old')

say_Name('Andrei',30)
say_Name()

# Return in functions auto exits the function
def sum(num1, num2):
    return num1 + num2

print(sum(2,3))

#Complex Function Structure
def add(x,y):
    def another_function(x,y):
        return x + y
    return another_function(x,y)

total = sum(10,20)
print(total)
def sub(num,num1):
    def innerFunction(n,n1):
        return n - n1
    return innerFunction(num,num1)

total = sub(20,10)
print(total)

