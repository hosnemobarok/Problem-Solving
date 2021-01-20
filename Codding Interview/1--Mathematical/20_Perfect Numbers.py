'''
    Time Complexity     : O(sqrt(N))
    Space Complexity    : O(1)
'''
from math import sqrt
def Perfect_Number(number):
    if number == 1:
        return 0

    sum = 1
    for i in range(2, int(sqrt(number)+1)):
        if number % i == 0:
            sum += (i + number // i)

    if sum == number:
        return 1
    else:
        return 0

# Driver code
if __name__ == '__main__':
    num = int(input())
    res = Perfect_Number(num)
    print(res)


'''
# User function Template for python3
from math import sqrt


class Solution:
    def isPerfectNumber(self, N):
        # code here
        if N == 1:
            return 0

        sum = 1
        #              2,  (N ** 0.5)
        for i in range(2, int(sqrt(N) + 1)):
            if N % i == 0:
                sum += (i + N // i)

        if N == sum:
            return 1
        else:
            return 0

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends
'''