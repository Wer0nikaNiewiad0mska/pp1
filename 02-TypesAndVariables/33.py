password = (input('Please, enter your password:')) #Must contain at least 8 characters
if len(password)<8:
    print('Password is valid: False')
else:
    print('Password is valid: True')