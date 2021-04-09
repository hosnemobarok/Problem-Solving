class Solution:

    def insertionSort1(self, arr):
        for k in range(0, n - 1):
            for i in range(0, n - 1):

                if arr[i] > arr[i + 1]:
                    temp = arr[i + 1]
                    arr[i + 1] = arr[i]

                    for j in arr:
                        print(j, end=" ")
                    arr[i] = temp

                    print()
        for j in arr:
            print(j, end=" ")


if __name__ == '__main__':
    op = Solution()
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    op.insertionSort1(arr)
