# problem link: https://leetcode.com/problems/bitwise-and-of-numbers-range/
"""
	Runtime: 56 ms, faster than 82.71% of Python3 online submissions for Bitwise AND of Numbers Range.
	Memory Usage: 14.2 MB, less than 81.56% of Python3 online submissions for Bitwise AND of Numbers Range.
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        res = 0
        while left != right:
            left >>= 1
            right >>= 1
            res += 1
        return left << res
