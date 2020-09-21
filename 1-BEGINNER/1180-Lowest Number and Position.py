#Accept
#https://www.urionlinejudge.com.br/judge/en/problems/view/1180

N = int(input())

x = list(map(int, input().split()))
m = min(x)
ind = []
for i in range(len(x)):
    if x[i] == m:
        ind.append(i)

print('Menor valor: %d'%m)
print('Posicao: {}'.format(*ind))

