import math
T = int(input())
for i in range(T):
    a,b,c = map(int, input().split())
    r = (a*b)//math.gcd(a,b)

    for x in range(r, c+1, r):
        print(x)
    if(i<T-1):
        print()