price = float(input('Enter the price: '))
discount = float(input('Enter the discount %: '))
new_price = price-(price*discount)/100
print(f'Reduction: {round(new_price,2)}')
reduction = (price*discount)/100
print(f'Price with discount: {round(reduction,2)}')