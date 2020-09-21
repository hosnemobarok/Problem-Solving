#Dimikoj Accept

import math
T = int(input())
for i in range(T):
    a,b,c = map(int, input().split())
    if (a+b>=c and b+c>=a and c+a>= b):
        s = (a + b + c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("%.2f"%area)
    else:
        print("Oh, No!")