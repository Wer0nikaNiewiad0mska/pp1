decimal=int(input('Enter the decimal number: '))

binary = [0] * decimal

i=0
while decimal>0:
    binary[i]=decimal%2
    decimal=int(decimal/2)
    i +=1

for j in range(i-1,-1,-1):
    print(binary[j], end="")
