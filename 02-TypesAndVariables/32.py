amount = float(input(f'Please, enter the amount: ')) #Entering the amount that was paid
vat = amount*0.23 #Calculating the VAT
round_vat = round(vat, 2)
print(f'Amount: {amount}')
print(f'VAT 23%: {round_vat}')