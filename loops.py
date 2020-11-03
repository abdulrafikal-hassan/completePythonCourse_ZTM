# loops 
for item in 'Zero to mastery':
    print(item)
print('end of loop')
# for varName in Iterabke: exprssion 

for i in (1,2,3,4,5):
    for x in ['a','b','c','d','e']:
        print(i, x)

# Iterable - list, dictionary, tuple, set, string
# Iterate - One by one check each item in the collection

user = {
    'name': 'Gotham',
    'age': 4550,
    'can_swim': False
}
# for keys of items 
for item in user:
    print(item)

for item in user.keys():
    print(item)

# for keys and values 
for item in user.items():
    print(item)

for key, value in user.items():
    print(key, value)

# For only values 
for item in user.values():
    print(item)


