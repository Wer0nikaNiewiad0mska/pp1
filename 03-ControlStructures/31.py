x=int(input('Enter the value of "x": '))
y=int(input('Enter the value of "y": '))

if x==0 and y==0:
    print(f'Point P({x},{y}) is located in position (0,0)')

if x==0:
    if y>0:
        print(f'Point P({x},{y}) is located on axis Y between the first and second quadrant')
    else:
        print(f'Point P({x},{y}) is located on axis Y between the third and fourth quadrant')

if y==0:
    if x>0:
        print(f'Point P({x},{y}) is located on axis X between the first and second quadrant')
    else:
        print(f'Point P({x},{y}) is located on axis Y between the third and fourth quadrant')

if x>0 and y>0:
    print(f'Point P({x},{y}) is located in first quadrant')

if x<0 and y>0:
    print(f'Point P({x},{y}) is located in second quadrant')

if x<0 and y<0:
    print(f'Point P({x},{y}) is located in third quadrant')

if x>0 and y<0:
    print(f'Point P({x},{y}) is located in fourth quadrant')