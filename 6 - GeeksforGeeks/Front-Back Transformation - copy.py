# User function Template for python3

class Solution:

    def convert(self, s):
        # code here

        d = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
             'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
             'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

        res = ''
        for i in s:
            if i.islower():
                res += d[i]

            elif i.isupper():
                c_l = i.lower()
                r = d[c_l]

                res += r.upper()

        return res


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.convert(s)

        print(ans)
# } Driver Code Ends


# 2nd code
s = 'HellO'

a = 'abcdefghijklmnopqrstuvwxyz'
b = 'zyxwvutsrqponmlkjihgfedcba'

up = []

inde = ''

for i in range(len(s)):
    if s[i].islower():

        inde += str(a.index(s[i]))
        #print(inde)
        inde += ' '

    if s[i].isupper():

        inde += str(a.index(s[i].lower()))
        #print(inde)

        inde += ' '

m = list(map(int, inde.split()))
#print(m)
solve = ''
for i in m:
    solve += b[i]

#print(solve)
ok = ""
for k in range(len(s)):
    if s[k].isupper():
        ok += solve[k].upper()
    else:
        ok += solve[k]
print(ok)
