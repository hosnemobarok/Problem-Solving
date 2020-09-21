# Accept..
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1073

N = int(input())

for i in range(2, N+1):
    if i % 2 == 0:
        print('%d^%d = %d'%(i, 2, pow(i, 2)))