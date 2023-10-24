'''
  Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
4.14. EXERCISES 55
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input.
'''

def computegrade():
    x=float(input('Enter score: '))
    if x>=0.9:
        print('A')
    elif x>=0.8 and x<0.9:
        print('B')
    elif x>=0.7 and x<0.8:
        print('C')
    elif x>=0.6 and x<0.7:
        print('D')
    else:
        print('F')

print(computegrade())