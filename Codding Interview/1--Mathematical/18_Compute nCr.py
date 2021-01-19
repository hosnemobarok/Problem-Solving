def Factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


def nCr(n, r):
    res = (Factorial(n) // (Factorial(r) * Factorial(n - r)))
    return res


# Driver Code
if __name__ == '__main__':
    n, r = map(int, input().split())
    res = nCr(n, r)
    print(res)

'''
# User function Template for python3

class Solution:

    def Factorial(self, n):
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac

    def nCr(self, n, r):
        mod = 1000000007
        res = (self.Factorial(n) // (self.Factorial(r) * self.Factorial(n-r)))
        return (res % mod)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends
'''