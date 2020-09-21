#Dimikoj Accept
for T in range(int(input())):
    X,N = map(int,input().split())
    if N < X:
        print('Invalid!')
    for i in range(1,N+1):
            if i % X == 0:
                print(i)
    print()