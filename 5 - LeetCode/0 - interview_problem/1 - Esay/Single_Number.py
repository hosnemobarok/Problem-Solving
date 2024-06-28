# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in nums:
            if nums.count(i) == 1:
                return i

        # res = 0
        # for i in nums:
        #     res ^= i
        
        # return res
