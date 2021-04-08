# User function Template for python3

class Solution:
    def count(self, s):
        # your code here
        upper_count = 0
        lower_count = 0
        numeric_count = 0
        special_count = 0
        for i in s:
            if i.isupper():
                upper_count += 1
            elif i.islower():
                lower_count += 1
            elif i.isnumeric():
                numeric_count += 1
            else:
                special_count += 1

        return upper_count, lower_count, numeric_count, special_count


# {
#  Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    s = input()
    ob = Solution()
    res = ob.count(s)

    for i in res:
        print(i)

# Contributed By: Pranay Bansal

# } Driver Code Ends