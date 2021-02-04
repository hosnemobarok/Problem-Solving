def Search_in_a_Rotated_Array(arr, k):
    if k not in arr:
        return -1


    return arr.index(k)


if __name__ == '__main__':
    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        res = Search_in_a_Rotated_Array(arr, k)
        print(res)