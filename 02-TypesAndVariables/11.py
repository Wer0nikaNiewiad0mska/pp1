fincome = float(input('Enter father`s income:'))
mincome = float(input('Enter mother`s income:'))
people = float(input('Enter number of people in family:'))
sum = fincome+mincome
print(f'Total income: {sum}')
pperson = sum/people
print(f'Income per person: {pperson}')