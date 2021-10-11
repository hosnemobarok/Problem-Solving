def aSolution():
    for _ in range(int(input())):
        m, n, k = map(int, input().split())

        total = n*k

        if m > total:
            print("YES")
        else:
            print("NO")

aSolution()