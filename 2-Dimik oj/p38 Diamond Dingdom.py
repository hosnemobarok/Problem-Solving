#Dimikoj not accept

for t in range(int(input())):
    n,m= map(int,input().split())
    for i in range(0, n+1):
        for j in range(0, i+1):
            print(m,end='')
        print()
    for i in range(n, 0, -1):
        for j in range(0, i-1):
            print(m,end='')
        print()