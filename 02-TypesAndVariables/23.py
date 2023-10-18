#Lenghts of the sides of the triangle
a = float(input('Enter the first side of the triangle:'))
b = float(input('Enter the second side of the triangle: '))
c = float(input('Enter the third side of the triangle:'))
#Calculating the circumference of a triangle
circumference = a+b+c
p = (a+b+c)/2
#Calculating the area of the triangle using the Heron formula
area = (p*(p-a)*(p-b)*(p-c))**0.5
#Displaying both area and circumference
print(f'Triangle circumference: {circumference}')
print(f'Triangle area: {area}')