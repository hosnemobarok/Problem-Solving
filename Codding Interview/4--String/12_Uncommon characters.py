# User function Template for python3

class Solution:
    def UncommonChars(self, A, B):
        # code here
        res = set(A) ^ set(B)
        ress = ''
        for i in sorted(res):
            ress += i

        if len(ress) > 0:
            return ress
        else:
            return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends