#Dimikoj Accept

T = int(input())
for i in range(1, T+1, 1):
    N = int(input())
    print("Case %d:"%i,end=" ")
    for j in range(1, N):
        if N % j == 0:
            print(j,end=' ')
    print(N)

