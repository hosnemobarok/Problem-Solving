#Dimikoj Accept

for i in range(int(input())):
    N = int(input())
    temp = N
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum +=(digit**3)
        temp = temp // 10
    if N == sum:
        print('%d is an armstrong number!'%N)
    else:
        print('%d is not an armstrong number!'%N)