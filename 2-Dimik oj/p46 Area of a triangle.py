#Dimikoj Accept

import math
T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area = %.3f"%area)