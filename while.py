#While loop 
i = 0
while 0 < 50:
    print(i)
    break
 
while i < 50:
     print(i)
     i += 1
else:
    print('done with all the work')

while True:
    response = input('say something: ')
    print(f'You said {response}')
    if(response == 'bye'):
        break
# continue restarts the function 
# pass continues the exe of a function