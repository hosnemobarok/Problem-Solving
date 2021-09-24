def Solution():

    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        if size == 1:
            print("YES")

        else:

            for i in range(size-1):
                if arr[i+1] - arr[i] > 1:
                    print("NO")
                    break
            else:
                print("YES")


Solution()
