#Accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1157

n = int(input())
for i in range(1, n+1):
    for j in range(1, n+1):
        if i * j == n:
            print(i)