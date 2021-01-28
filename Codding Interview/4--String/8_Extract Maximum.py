"""
    Input:
    S = 100klh564abc365bg

    Output: 564
    Explanation: Maximum numeric value
    among 100, 564 and 365 is 564.

    Input:
    S = abcdefg
    Output: -1

    Explanation: Return -1 if no numeric
    value is present.
"""


#User function Template for python3

class Solution:
    def extractMaximum(self,S):
        # code here
        if S.isalpha():
            return -1

        else:
            res = ""
            for i in range(len(S)):
                if S[i].isdigit():
                    res += S[i]
                else:
                    res += " "

            return max([int(x) for x in res.split()])

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        print(ob.extractMaximum(S))

# } Driver Code Ends