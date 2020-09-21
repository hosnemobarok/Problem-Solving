#Dimikoj Accept
T = int(input())
for i in range(T):
    X, K = map(int, input().split())
    sum = 1
    power = 1
    for j in range(1, K+1):
        power = power * X
        sum += power

    print('Result =',sum)



#2nd Rules
c = 0
a,b = map(int, input().split())
for i in range(b+1):
    c += a**i
print('Result =',c)