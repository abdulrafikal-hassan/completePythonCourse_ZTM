##last but One  tutorial in Python I folder
#Tuple are immutable List 
my_tuple = (1,2,3,4,5)
print(my_tuple[2])
print(4 in my_tuple)
user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    'age': 20
}

print(user[(1,2)])
print(user['greet'])
print(user['age'])

new_tuple = my_tuple[1:3]
print(new_tuple)
x,y,z, *other = (1,2,3,4,5)
print(x)
print(y)
print(z)
print(other)
print(my_tuple.index(4))
print(len(my_tuple))