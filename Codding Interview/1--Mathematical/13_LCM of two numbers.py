
def gcd(x, y):

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):

   lcm = (x*y)//gcd(x,y)
   return lcm


# Driver Code
if __name__ == '__main__':
     x, y = map(int, input().split())
     print(lcm(x, y), gcd(x, y))

'''
# User function Template for python3
from math import lcm, gcd

class Solution:
    def lcmAndGcd(self, A, B):
        return lcm(A, B), gcd(A, B)


# code here


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = map(int, input().split())

        ob = Solution()
        ptr = ob.lcmAndGcd(A, B)

        print(ptr[0], ptr[1])
# } Driver Code Ends

'''