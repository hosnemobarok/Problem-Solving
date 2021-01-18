from math import gcd


def GCD(A, B):
    return gcd(A, B)


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))

'''
# Using Recursion :
def GCD(A, B):
    if B == 0:
        return A

    else:
        return GCD(B, A%B)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))

----------------------------------------------- 
# Using Loop :
def GCD(A, B):
    if A > B:
        small = B
    else:
        small = A
    for i in range(1, small+1):
        if (A % i == 0) and (B % i == 0):
            gcd = i

    return gcd

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))

------------------------------------------------
# Using Euclidean Algorithm
def GCD(A, B):
    while B:
        A, B = B, A % B

    return A

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))
'''
#################################################

from math import gcd


def GCD(A, B):
    return gcd(A, B)


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))

'''
# Using Recursion :
def GCD(A, B):
    if B == 0:
        return A

    else:
        return GCD(B, A%B)

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))

----------------------------------------------- 
# Using Loop :
def GCD(A, B):
    if A > B:
        small = B
    else:
        small = A
    for i in range(1, small+1):
        if (A % i == 0) and (B % i == 0):
            gcd = i

    return gcd

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))

------------------------------------------------
# Using Euclidean Algorithm
def GCD(A, B):
    while B:
        A, B = B, A % B

    return A

if __name__ == '__main__':
    A, B = map(int, input().split())
    print(GCD(A, B))
'''

###################################################
'''

#User function Template for python3
from math import gcd
class Solution:
    def gcd(self, A, B):
        # code here
        return gcd(A, B)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        A,B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A,B))
# } Driver Code Ends

'''
