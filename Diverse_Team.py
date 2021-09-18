# Solve
def aSolution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    conv = list(set(arr))
    if len(conv) >= m:
        print("YES")

        for i in range(m):
            num = conv[i]
            print(arr.index(num) + 1, end=" ")
    else:
        print("NO")

aSolution()
