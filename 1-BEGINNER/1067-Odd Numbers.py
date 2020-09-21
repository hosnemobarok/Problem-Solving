#accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1067

x = int(input())
for i in range(1, x+1):
    if i % 2 == 0:
        continue
    print(i)