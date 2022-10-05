"""
    problem link: -> https://leetcode.com/problems/removing-stars-from-a-string/description/

    time complexity     : O(n)
    space complexity    : O(1)

"""

class Solution:
    def removeStars(self, s: str) -> str:

        res = ""

        for ch in s:
            if ch == "*":
                res = res[:-1]

            else:
                res += ch
        
        return res
