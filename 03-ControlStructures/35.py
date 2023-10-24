num=1
for num in range(0,31):
        num+=1
        if num%3==0 and num%5==0:
            print(str(num)+" BINGO", end = " ")

        if num%3==0 and not num%5==0:
            print(str(num)+" THREE", end = " ")

        if num%5==0 and not num%3==0:
            print(str(num)+" FIVE", end = " ")
        
        if not num%3==0 or not num%5==0:
             print(str(num), end = " ")