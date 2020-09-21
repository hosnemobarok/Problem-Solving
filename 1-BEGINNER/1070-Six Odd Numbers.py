#Accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1070

x = int(input())

for i in range(x, (x+12)):
    if i % 2 == 0:
        continue
    else:
        print(i)