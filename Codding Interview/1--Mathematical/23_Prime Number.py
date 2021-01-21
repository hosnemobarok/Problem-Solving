
#  N check if it is prime or not
def is_Prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    # 2 skip all even number is'n prime.
    if n > 2 and n % 2 == 0:
        return False

    root = int((n ** 0.5))

    for i in range(3, root+1, 2):
        if n % i == 0:
            return False

    return True

# Driver Code
if __name__ == '__main__':
    n = int(input())
    res = is_Prime(n)
    print(res)




'''
#User function Template for python3

class Solution:
    def isPrime (self, N):
        # code here
        
        if N <= 1:
            return 0
        
        if N == 2:
            return 1
            
        if N > 2 and N % 2 == 0:
            return 0
            
        root = int(N ** 0.5)
        for i in range(3, root+1, 2):
            if N % i == 0:
                return 0
                
        return 1
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends
'''
