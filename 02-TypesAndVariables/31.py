import random

dice = random.randrange(1, 6) #Rolling the dice by computer
guess = int(input('Enter the number 1-6: ')) #Guessing the number
if dice == guess:
    print(f'Congratulations! You guessed correctly. The number is: {dice}')
else:
    print(f'Unortunately, your answer is wrong. The correct number is: {dice}')