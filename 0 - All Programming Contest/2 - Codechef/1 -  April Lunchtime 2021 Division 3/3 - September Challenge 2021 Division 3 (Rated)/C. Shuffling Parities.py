for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    res = []

    even = odd = 0

    for i in arr:
        if i % 2 == 1:
            odd += 1

        else:
            even += 1

    solve = min(odd, n//2) + min(even, (n+1)//2)
    print(solve)