#Entering the data
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m:'))
#Calculating the BMI index
bmi = weight/height**2
print(f'Your BMI index: {bmi}')
#Checking whether the weight is in the valid range
if bmi<18.5:
    print('Correct BMI: False')
elif bmi>24.9:
    print('Correct BMI: False')
else:
    print('Correct BMI: True')