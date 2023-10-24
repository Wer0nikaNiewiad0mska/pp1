rows = 5

for i in range(rows+1):
    for j in range(i):
        j="*"
        print(j, end=' ')
    print('')

rows = 4
b=0

for i in range(rows, 0, -1):
    b+=1
    for j in range(1, i+1):
        j='*'
        print(j, end = " ")
    print('\r')