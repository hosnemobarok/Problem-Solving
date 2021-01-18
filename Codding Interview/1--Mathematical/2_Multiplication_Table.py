
def Multiplication_Table(N):
    mul = []
    for i in range(1, 11):
        mul.append(N * i)
    return mul

if __name__ == '__main__':
    N = int(input())
    print(Multiplication_Table(N))


'''
# User function Template for python3

class Solution:
    def getTable(self, N):
        # code here

        mul = []
        for i in range(1, 11):
            mul.append(N * i)
        return mul

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.getTable(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
'''