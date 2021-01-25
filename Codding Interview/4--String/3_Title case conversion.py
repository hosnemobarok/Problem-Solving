def solve(string):
    return string.title()



def Upper_cas_conversion(string):
    res_string = ""
    res_string = string[0].upper()

    for ch in range(1, len(string)):
        if string[ch - 1] == " ":
            res_string += string[ch].upper()

        else:
            res_string += string[ch]

    return res_string


if __name__ == '__main__':
    string = input()

    #res = solve(string)

    res = Upper_cas_conversion(string)
    print(res)

"""
#User function Template for python3

class Solution:
    def transform(self, s):
        # code here

        res_string = ""
        res_string = s[0].upper()

        for ch in range(1, len(s)):
            if s[ch-1] == " ":
                res_string += s[ch].upper()

            else:
                res_string += s[ch]

        return res_string


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends
"""