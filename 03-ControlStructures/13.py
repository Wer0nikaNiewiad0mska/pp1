first_number = int(input('Enter number 1: '))
second_number = int(input('Enter second number: '))

if first_number>=0 or second_number>=0:
    print(f'At least one of the numbers {first_number} and {second_number} is not negative')
else:
    print(f'At least one of the numbers {first_number} and {second_number} is negative or both')