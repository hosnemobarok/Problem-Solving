def inserting_sort_2(arr):
    n = len(arr)
    for i in range(1, n):

        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        print(' '.join(str(j) for j in arr))


if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().split()))
    inserting_sort_2(arr)
