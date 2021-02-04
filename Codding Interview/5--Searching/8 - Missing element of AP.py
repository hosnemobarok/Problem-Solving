# User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        # code here

        mis = arr[1] - arr[0]

        res = 0
        for i in range(0, n - 1):
            if arr[i] + mis < arr[i + 1]:
                res += arr[i] + mis
                break

        return res


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMissing(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends