# writing the complete Error handling try block 

while True:
    try:
        age = int(input('what is your age? '))
        10 / age
# creating your own errors
        # raise Exception('when u want to create ur own lib')
        # raise ValueError('This is my own error')
    except ValueError:
        print('Please entre a number')
        continue 
    except ZeroDivisionError:
        print(' Please enter age higher than 0')
        break
    else: 
        print('thank you ')
        break # this break fun stops finally from running
    finally:
        print('Ok, I am finally done. End of the try block')
    
    print('Can you hear me. 4rm the loop block')