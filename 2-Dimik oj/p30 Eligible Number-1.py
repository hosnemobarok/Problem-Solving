#Dimikoj Accept
li=[6,28,496,8128,33550336]
for T in range(int(input())):
    N = int(input())
    if N in li:
        print("YES,",N,"is a perfect number!")
    else:
        print("NO,",N,"is not a perfect number!")




#2nd Rules
import math
for T in range(int(input())):
    N = int(input())
    sq, sum = int(math.sqrt(N)), 1
    for i in range(2, sq+1):
        if N % i == 0:
            sum += (N//i) + i
        if sum > N:
            break
    if sum == N:
        print("YES, %d is a perfect number!"%N)
    else:
        print("NO, %d is not a perfect number!"%N)