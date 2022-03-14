class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 2:
            return nums
        
        res = []
        
        for i in range(len(nums)):
            
            if nums.count(nums[i]) == 1:
                res.append(nums[i])
        
        return res
                    
