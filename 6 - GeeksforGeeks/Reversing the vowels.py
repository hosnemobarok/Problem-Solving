# User function Template for python3

class Solution:
    def modify(self, s):
        # code here

        s = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u']

        v = []

        for i in range(len(s)):
            if s[i] in vowel:
                v.append(s[i])
                s[i] = '0'

        v = v[::-1]

        solve = ""
        for j in range(len(s)):
            if s[j] == '0':
                solve += v[0]
                v.remove(v[0])

            else:
                solve += s[j]
        return solve


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends