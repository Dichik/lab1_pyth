import math

print('Enter coordinate of x1: ')
x1 = int(input())
print('Enter coordinate of y1: ')
y1 = int(input())
print('Enter coordinate of x2: ')
x2 = int(input())
print('Enter coordinate of y2: ')
y2 = int(input())
ans = float(math.sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ) )
print('The distance between two poits equal to: ')
print(ans)

