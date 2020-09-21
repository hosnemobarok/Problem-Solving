#Dimikoj Accept

from math import gcd
for T in range(int(input())):
    a,b = map(int, input().split())
    print('LCM =',(a*b//gcd(a,b)))