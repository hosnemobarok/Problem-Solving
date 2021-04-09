class Solution:

    def Running_Time(self, arr):
        lenght = len(arr)

        count = 0
        for i in range(0, lenght):
            item = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > item:
                arr[j+1] = arr[j]
                j -= 1
                count += 1
            arr[j+1] = item
        return count



if __name__ == '__main__':
    op = Solution()

    n = int(input())
    arr = list(map(int, input().split()))
    print(op.Running_Time(arr))
