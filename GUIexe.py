picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for image in picture:
    for pixel in image:
        if (pixel == 1):
            print('*', end= '')
        else:
            print(' ', end='')
    print('')

#Writing of Good Code 
# Clean, Readable, Predictability, DRY

fill = "^"
empty = ' '

for row in picture:
    for pixel in row:
        if(pixel):
            print(fill, end= empty)
        else:
            print(empty, end= empty)
    print(empty)

    #Clean Code
    #checking to see if it is even or not
def is_even(num):
    return num % 2 == 0
print(is_even(50))

# Or another Clean Code 
def is_odd(num):
    if num % 2 != 0:
        return True
    return False
print(is_odd(3))
print(is_odd(4))