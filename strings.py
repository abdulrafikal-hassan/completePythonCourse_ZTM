some_string = 'hello there'
print(type(some_string))

user_name = "supercoder"
password = "supersecret"

long_string = '''
WOW
0 0
---

'''
print('this is your name '+ user_name)
print('this is your password '+password)
print(long_string)

first_name = "Al-hassan"
last_name = "Abdul Rafik"

full_name = first_name + ' ' + last_name
print(full_name)

#String Concatenation (adding of strings together)
print(100)
print(type(str(100)))
print(type(int(str(1000))))

#Escape Sequence 
weather = "It's \"kind of\" sunny today"
print(weather)


#Formatted Strings 

name = 'Johnny'
age = 55
print('hi ' + name + ' you are '+ str(age) + ' years old')

# or the formaatted way best practice 

print(f'hi {name}, You are {age} years old')

#another way of using formatted method 

print('hi {}. You are {} of age'.format(name,age))

#String Indexes 

selfish = '0123456789'
        #  01234567
#selfish['start', 'end', 'stepover']
print(selfish[0:5:2])

# another way reversing using indexes
print(selfish[::-1])

##Immutabilty
#strings in python are immutable == they cant be changed 

