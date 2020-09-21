#Dimikoj Accept

T = int(input())
for i in range(T):
    N =int(input())
    F = 1
    for j in range(1, N+1):
        F *= j
    print(F)



#2nd Rules
from math import factorial

factor = factorial(int(input()))
print(factor)