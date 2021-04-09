def Bubble_sort(arr):
    length = len(arr)

    for i in range(0, length - 1):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(*arr)
    exit()

if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().split()))
    print(Bubble_sort(arr))
