def ReverseArray(arr):
    print(*arr[::-1])


# Driver Code:
if __name__ == "__main__":
    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))
        ReverseArray(arr)