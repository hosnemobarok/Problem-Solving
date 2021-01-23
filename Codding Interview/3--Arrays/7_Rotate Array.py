
def Rotate_Array(D, arr):
    rotate = arr[D:] + arr[:D]
    print(*rotate)


if __name__ == "__main__":
    for _ in range(int(input())):
        N, D = map(int, input().split())
        arr = list(map(int, input().split()))
        Rotate_Array(D, arr)