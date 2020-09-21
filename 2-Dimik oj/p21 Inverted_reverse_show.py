#dimikoj accpet

T = int(input())
for i in range(T):
    S = input()
    C = S.split()
    print(S[::-1])



#2nd Rules

T = int(input())
for i in range(T):
    str = input()
    if len(str) <= 100:
        print(str[::-1])
    else:
        break