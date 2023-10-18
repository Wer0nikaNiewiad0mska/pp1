#Entering the age
age = int(input('Enter age: '))
#checking if a person is exempt from paying taxes
if age <= 26:
    print('Exception from paying taxes: True')
else:
    print('Exception from paying taxes: False')
