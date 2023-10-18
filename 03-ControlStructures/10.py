number = int(input('Enter number: '))

if number>=0:
    print(f'|{number}| = {number}')
else:
    print(f'|{number}| = {number*-1}')
#Można też zrobić "if x>=0; print(x);else: print(-x)"