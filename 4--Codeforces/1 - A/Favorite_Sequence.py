def Solution():
    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))

        left = 0
        right = size - 1
        if size % 2 != 0:
            res = []
            while left <= right:
                res.append(arr[left])
                res.append(arr[right])
                left += 1
                right -= 1

            print(*res[:-1])

        else:
            res = []
            while left <= right:
                res.append(arr[left])
                res.append(arr[right])
                left += 1
                right -= 1

            print(*res)

Solution()
