'''
    Time Complexity     : O(sqrt(N))
    Space Complexity    : O(1)
'''
def Perfect_Number(number):
    if number <= 1:
        return 0

    sum = 1
    sqrt = int(number ** 0.5)
    for i in range(2, sqrt+1):
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

class Solution:
    def isPerfectNumber(self, N):
        # code here
        if N <= 1:
            return 0
            
        sum = 1
        sqrt = int(N ** 0.5)
        for i in range(2, sqrt+1):
            if N % i == 0:
                sum += (i + N // i)
                
        if sum == N:
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
