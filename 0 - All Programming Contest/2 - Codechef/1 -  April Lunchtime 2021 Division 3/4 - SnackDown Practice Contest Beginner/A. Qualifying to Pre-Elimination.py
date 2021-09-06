def A_solve():
    for _ in range(int(input())):
        k, n = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()

        li = arr[::-1]
        res = li[n-1]

        count = 0
        for i in li:
            if i >= res:
                count += 1
        print(count)

A_solve()