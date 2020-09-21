#accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1165

for N in range(int(input())):
    x = int(input())
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                print('%d nao eh primo'%x)
                break
        else:
            print('%d eh primo'%x)
    else:
        print('%d nao eh primo'%x)
