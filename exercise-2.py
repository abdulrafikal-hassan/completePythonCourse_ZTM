user_name = input('Enter your name: ')
password = input('Enter your password: ')
enc_password = len(password) * '*'
print(user_name)
print(f'your password {enc_password} is {len(password)} characters long')
