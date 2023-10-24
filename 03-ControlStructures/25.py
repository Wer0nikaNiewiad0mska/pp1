products = int(input('Number of products purchased: '))
p = float(input('Product price: '))

if products>=0 and products<=2:
    print(f'Amount to pay: {p*products}')
elif products>2:
    price1 = (p*0.75)*(products-2)+(2*p)
    print(f'Amount to pay: {price1}')