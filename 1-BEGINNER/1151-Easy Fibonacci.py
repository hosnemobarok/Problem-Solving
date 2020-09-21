#not accept
#link:https://www.urionlinejudge.com.br/judge/en/problems/view/1151

def fib(N):
    n1,n2, count = 0, 1, 0
    while count < N:
        print(n1, end=' ')
        nth = (n1+n2)
        n1 = n2
        n2 = nth
        count += 1
    print(n1)
    exit()

if __name__=="__main__":
    N = int(input())
    print(fib(N))