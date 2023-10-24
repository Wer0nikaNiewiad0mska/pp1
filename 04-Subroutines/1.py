'''
Using built-in Python functions, write a program that calculates and displays:
a.	length of the phrase: "computer science"
b.	letter read from the keyboard
c.	string representing the number 5068
d.	numeric representing the string "20303"
e.	the smallest number given: 4,7,2,3,9,8
'''

a='computer science'
x=len(a)
print(f'The lenght od {a} is: {x}')

b=input('Enter a letter from a keyboard: ')
print(f'{b}')

c=str(5068)
print(c)

d=int(20303)
print(d)

e=min(4,7,2,3,9,8)
print(e)