is_old = True
is_licenced = True 

if is_old and is_licenced:
    print('you are old enough to drive and you have a licence')
# elif is_licenced:
#     print('you can drive now!')
else:
    print('you are not of age!')

print('okoko')

# Truthy and Falsy 
is_old = bool('hello')
is_licenced = bool(5)

print(bool(''))
print(bool(None))

password = '123'
username = 'johnny'

if password and username:
    print('You are welcome Johnny')
else:
    print('your password or username isincorrect')
print('end of Truthy and Falsy Tuts')

# Ternary Operators = Conditional Epressions

# condition_if_true if condition else condition_if_false
is_friend = True
can_message = " message allowed" if is_friend else "not allowed to message"
print(can_message)
print('End of Ternary Operators!!!')

# Short Circuiting 
is_friend = True
is_user = True 

if is_friend and is_user:
    print('best friends forever')

print('End of short circuiting!')

#Logical Operators
print(4 == 5)
print('a' > 'b')
print( 'a' > 'A')

print(not(True)) ## False != == not() 
