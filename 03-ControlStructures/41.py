guess=input('Enter the PIN code: ')
code = '0805'

if not guess==code:
    print('Incorrect...')
    print(input('Enter the PIN code: '))
else:
    print('Correct')