amount = int(input('Enter the amount in PLN: '))

piec=1

i=0
while amount%5==0:
    piec[i]=amount/5
    i +=i
    print(f'The amount of {amount} PLN in coins:')
    print(f'5 zl - {piec}')

