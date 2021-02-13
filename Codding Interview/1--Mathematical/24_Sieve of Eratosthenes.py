
# All prime number [2.......N]
def SieveOfEratosthenes(n):

    prime = [True]*(n+1)

    p = 2

    while (p*p <= n):

        if prime[p] == True:

            # 4 to n+1 all even number False [not prime number]
            for i in range(p*p, n+1, p):
                prime[i] = False

        p += 1

    # print all prime number
    for j in range(2, n+1):
        if prime[j]:
            print(j, end=' ')


# Driver Code
if __name__ == '__main__':
    n = int(input())
    SieveOfEratosthenes(n)



'''
class Solution:
    def sieveOfEratosthenes(self, N):
        # code here

        prime = [True] * (N + 1)

        p = 2

        while (p * p <= N):

            if prime[p] == True:
                for i in range(p * p, N + 1, p):
                    prime[i] = False

            p += 1

        ans = []
        for j in range(2, N+1):
            if prime[j]:
               ans.append(j)

        return ans

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
'''
