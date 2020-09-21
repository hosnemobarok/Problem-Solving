#Dimikoj Accept

for t in range(int(input())):
    A, B, C = map(int, input().split())
    if A % C == 0:
        for i in range(A, B+1, C):print(i)
    else:
        for j in range(A, B+1):
            if j % C == 0:print(j)
    print()