#Dimikoj Accept
for T in range(int(input())):
    n = sorted(list(map(int,input().split())))
    print('Case %d:'%(T+1),*n)


#Dimikoj 2nd code
T = int(input())
for i in range(1, T):
    li = sorted(list(map(int, input().split())))
    print('Case %d: '%i,end='')

    for x in range(len(li)):
        if(x<len(li)-1):
            print(li[x],end=' ')
        else:
            print(li[x])