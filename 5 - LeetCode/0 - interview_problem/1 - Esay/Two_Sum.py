# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        n = len(nums)

        for i in range(n):
            for j in range(1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """
        
        seen = {}

        for (index,  value) in enumerate(nums):
            remaining = target - nums[index]

            if remaining in seen:
                return [index, seen[remaining]]
            else:
                seen[value] = index
