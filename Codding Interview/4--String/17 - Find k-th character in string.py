def Find_kth_character_in_string(m, n, k):

    binary = bin(m)[2:]

    for i in range(n):
        binary = binary.replace('1', 'X').replace('0', '01').replace('X', '10')

    return binary[k-1]



if __name__ == '__main__':
    m, n, k = map(int, input().split())

    res = Find_kth_character_in_string(m, n, k)
    print(res)


"""
# User function Template for python3
class Solution:
    def kthCharacter(self, m, n, k):
        # code here

        binary = bin(m)[2:]
        for i in range(n):
            binary = binary.replace('1', 'X').replace('0', '01').replace('X', '10')

        return binary[k - 1]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, n, k = input().split()
        m, n, k = int(m), int(n), int(k)

        ob = Solution()
        answer = ob.kthCharacter(m, n, k)
        print(answer)

# } Driver Code Ends
"""