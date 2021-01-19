def Factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i

    return fac


# create nPr function
def nPr(n, r):

    res = (Factorial(n) // Factorial(n-r))
    return res

# Driver Code
if __name__ == '__main__':
    n, r = map(int, input().split())
    res = nPr(n, r)
    print(res)



'''
# User function Template for python3

class Solution:
    def Factorial(self, n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac

    def nPr(self, n, r):
        # code here

        res = (self.Factorial(n) // self.Factorial(n - r))
        return res


# { 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.nPr(n, r))
# } Driver Code Ends
'''