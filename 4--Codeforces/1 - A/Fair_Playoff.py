def Solution():
    for _ in range(int(input())):
        a, b, c, d = map(int, input().split())

        res = [a, b, c, d]
        l = [a, b, c, d]

        aMax = max(l)
        l.remove(aMax)
        bMax = max(l)
        l.remove(bMax)

        s = sorted(res)[2:]

        left = sorted([a, b])
        right = sorted([c, d])

        if s == left or s == right:
            print("NO")
        else:
            print("YES")
Solution()