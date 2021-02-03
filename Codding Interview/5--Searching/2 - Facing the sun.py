def countBuildings(size, arr):
    # code here
    if arr == sorted(arr):
        return size

    else:

        big = arr[0]
        count = 1

        for i in range(1, size):
            if arr[i] > big:
                count += 1

                big = arr[i]

        return count


if __name__ == '__main__':
    size = int(input())
    arr = list(map(int, input().split()))
    res = countBuildings(size, arr)
    print(res)





"""
# User function Template for python3
class Solution:

    def countBuildings(self, h, n):
        # code here
        if h == sorted(h):
            return len(h)

        else:

            big = h[0]
            count = 1

            for i in range(1, n):
                if h[i] > big:
                    count += 1

                    big = h[i]

            return count


# { 
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends"""