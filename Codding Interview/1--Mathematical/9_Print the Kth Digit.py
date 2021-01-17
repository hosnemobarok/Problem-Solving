def KthDigit(A, B, K):

    pw = pow(A, B)
    pw_string = str(pw)[::-1]
    return pw_string[K-1]


if __name__ == '__main__':
   for _ in range(int(input())):
       A, B, K = map(int, input().split())
       KthDigit(A, B, K)

'''
#User function Template for python3
class Solution:
    def kthDigit(self, A, B, K):
        # code here
        pw  = pow(A, B)
        pws = str(pw)[::-1]
        return pws[K-1]


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        A,B,K = input().split()
        ob = Solution()
        print(ob.kthDigit(int(A),int(B),int(K)))
# } Driver Code Ends

'''