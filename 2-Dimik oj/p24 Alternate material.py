#Dimikoj Accept

T = int(input())
for i in range(T):
    n = int(input())
    li = list(map(int, input().split()))

    for j in range(0, n, 2):
        print(li[j], end='')
        if(j<n-2):
            print(' ',end='')
    print()