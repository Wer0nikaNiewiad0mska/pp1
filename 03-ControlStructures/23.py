human_years = int(input('Enter dog`s age in human years: '))

if human_years<=2:
    doggy1 = int(human_years*10.5)
    print(f'The dog`s age in dog`s years is: {doggy1}')
else:
    doggy2 = int((human_years-2)*4+2*10.5)
    print(f'The dog`s age in dog`s years is: {doggy2}')