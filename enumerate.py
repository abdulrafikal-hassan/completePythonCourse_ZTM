# enumerate also loops over items and can add indexes counter
for i,char in enumerate('helloWorld'):
    print(i, char)

for i, num in enumerate([1,2,3,4]):
    print(i, num)

for key,num in enumerate(list(range(100))):
    print(key,num)
    if num == 50:
        print(f'Index of 50 is : {key}')
