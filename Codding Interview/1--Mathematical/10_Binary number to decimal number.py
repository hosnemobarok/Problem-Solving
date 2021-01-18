
def BinaryToDecimal_num(str):
    return int(str, 2)


if __name__ == '__main__':
    str = input()
    print(BinaryToDecimal_num(str))


'''
# User function Template for python3

class Solution:
    def binary_to_decimal(self, str):
        return int(str, 2)

# Code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        ob = Solution();
        ans = ob.binary_to_decimal(str)
        print(ans)
# } Driver Code Ends
'''