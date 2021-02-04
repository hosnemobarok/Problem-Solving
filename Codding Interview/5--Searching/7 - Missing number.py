def Missing_Number(arr, size):

    res = [x for x in range(1, size+ 2)]
    res = list(set(res) ^ set(arr))
    print(res[0])


if __name__ == "__main__":
    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))

        Missing_Number(arr, size)




def Missing_Number(arr, size):

    n = size + 1
    res = n*(n+1) // 2

    return res - sum(arr)


if __name__ == "__main__":
    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))

        res = Missing_Number(arr, size)
        print(res)