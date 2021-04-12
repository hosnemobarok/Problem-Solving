
def getSum(n, m):

    res = ""
    while n != 0:
        digit = (n % 10) + m

        res += str(digit)
        res += ' '

        n //= 10



    ok = res.split()[::-1]
    okk = "".join(x for x in ok)

    print(len(okk))



for _ in range(int(input())):
    n, m = map(int, input().split())
    getSum(n, m)
