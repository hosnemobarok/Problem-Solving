def Solution():
    x1, x2, x3 = map(int, input().split())
    arr = sorted([x1, x2, x3])
    Min = arr[0]
    Max = arr[-1]
    mid = arr[1]

    li = [x for x in range(Min, Max+1)]

    left = li[:mid]
    right = li[mid:]
    res = (len(left)-1) + len(right)
    print(res)

# Drive Code
Solution()