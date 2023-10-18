#The height in cm
cm = int(input('Enter your height in cm:'))
#Converting the height to feet and inches 
feet = cm//30.48
inches = cm%30.48
round = round(inches,0)
#Displaying the result
print(f'I am {cm}cm tall, i.e. {feet} feet and {round} inches')