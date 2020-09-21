#Accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1164

for N in range(int(input())):
    x = int(input())
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    if s == x:
        print('%d eh perfeito'%x)
    else:
        print('%d nao eh perfeito'%x)