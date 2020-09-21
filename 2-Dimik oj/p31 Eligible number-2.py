#Dimikoj Accept
T = int(input())
for i in range(T):
    perf = [6, 28, 496, 8128, 33550336]

    number = int(input())
    for j in perf:
        if j <= number:
            print(j)
    if i < T - 1:
        print()


#Time Time Limit Exceeded
'''T = int(input())
for x in range(T):
    limit = int(input())

    for n in range(2, limit + 1):
        sum = 0
        for i in range(1, n):
            if not n % i:
                sum += i
        if sum == n:
            print(n)
    if(x<T-1):
        print()

'''