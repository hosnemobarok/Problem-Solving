# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digit = 0

        for i in digits:
            digit = 10 * digit + i
        
        plusOne = digit + 1

        return [int(x) for x in str(plusOne)]
