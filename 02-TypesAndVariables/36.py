buys = float(input('Bank buys EUR:'))
sells = float(input('Bank sells EUR:'))
#Calculating the spread 
spread = sells-buys
r = round(spread, 4) #Rounding the spread
print(f'Spread: {r}')