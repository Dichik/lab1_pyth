import math

x1 = float(input('Enter coordinate of x1: '))
y1 = float(input('Enter coordinate of y1: '))
x2 = float(input('Enter coordinate of x2: '))
y2 = float(input('Enter coordinate of y2: '))
ans = float(math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ) )
print('The distance between two poits equal to: ')
print(ans)

