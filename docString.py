#docStrings 

def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)

test('!!!!')

#Or use the help to find out what a function does
help(test)

#Or use a magic method
print(test.__doc__)
#This is custom documentation of strings 