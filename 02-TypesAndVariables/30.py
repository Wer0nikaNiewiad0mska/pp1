import random #Not sure what it does
dice = random.randrange(1, 6) #Rolling the dice
print(f'The number you got: {dice}')
if dice == 1 or dice == 6:
    print('Special numer: Yes')
else:
    print('Special number: No')