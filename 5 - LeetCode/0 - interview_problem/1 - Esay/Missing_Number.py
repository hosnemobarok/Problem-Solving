# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        sum_expected = n * (n + 1) // 2
        missing_number = sum_expected - sum(nums)
        return missing_number
        
        
        

