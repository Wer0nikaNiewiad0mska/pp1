'''
 Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
def computepay(hrs,rate):
    pay = float(hrs)*float(rate)
    print(pay)

print(computepay(4,56))