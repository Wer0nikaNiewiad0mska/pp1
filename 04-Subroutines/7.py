'''
Define an anonymous function that calculates the body mass index (BMI) for the given weight in kg and height in cm. Then, calculate the BMI for Peter (81kg, 182cm). Sample result:
Peter`s BMI is …
'''

lambda x, y: x/y**2

g=lambda x, y:x/y**2
print('Peter`s BMI is...', g(56, 1.64))
