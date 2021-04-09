class Solution:

    def Sherlockarndarray(self, arr):
        left_index = 0
        right_index = len(arr) - 1


        left_sum = arr[left_index]
        right_sum = arr[right_index]


        while left_index != right_index:

            if left_sum < right_sum:
                left_index += 1
                left_sum += arr[left_index]

            else:
                right_index -= 1
                right_sum += arr[right_index]

        return left_sum == right_sum



if __name__ == '__main__':
    op = Solution()

    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        if op.Sherlockarndarray(arr):
            print('YES')
        else:
            print("NO")
