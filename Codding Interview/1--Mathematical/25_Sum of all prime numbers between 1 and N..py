def Prime_sum(n):
    prime = [True] * (n + 1)

    p = 2

    while (p * p <= n):

        if prime[p] == True:

            # 4 to n+1 all even number False [not prime number]
            for i in range(p*p, n + 1, p):
                prime[i] = False

        p += 1

    sum = 0
    # print all prime number
    for j in range(2, n + 1):
        if prime[j]:
            sum += j

    return sum


# Driver Code
if __name__ == '__main__':
    n = int(input())
    res = Prime_sum(n)
    print(res)

'''
#User function Template for python3

class Solution:
	def prime_Sum(self, n):
		# Code here
		prime = [True] * (n + 1)

        p = 2

        while (p * p <= n):

            if prime[p] == True:
                for i in range(p * p, n + 1, p):
                    prime[i] = False

            p += 1

        ans = 0
        for j in range(2, n+1):
            if prime[j]:
               ans += j

        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.prime_Sum(n)
		print(ans)
# } Driver Code Ends
'''
