#Dictionary can be called object,map or array
#dict is a way to organise your data, is an ordered key value pair

dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': [1,2,3,4,5]
}

my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4,5,6],
        'b': 'good day',
        'x': False
    }
]

print(dictionary['c'])
print(dictionary)
print(my_list[0]['a'][2])
print(my_list[1]['b'][1])

#Dictionary keys tuts
# keys are unique and cant be changed 
print(dictionary['d'])

user = {
    'name': 'this is myname',
    'age': [1,2,3] 
}

print(user.get('age', 'default'))

user2 = dict(name='JohnDoe')
print(user2)

#Dictionary Methods 

print('Jothndoe' in user2)

print('Good' in user.items())
print(user.items())
user3 = user.copy()
print(user.clear())

print(user3.popitem())
