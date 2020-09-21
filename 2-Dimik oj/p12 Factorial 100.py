#Dimikoj Accept

from math import factorial

for T in range(int(input())):
    c = 0
    N  = factorial(int(input()))

    while N > 0:
        mod = N % 10
        if (mod == 0):
            c += 1
        else:
            break
        N = N // 10
    print(c)



#2nd Rules
for T in range(int(input())):
    N = int(input())
    result = (N//5)+(N//25)
    print(result)