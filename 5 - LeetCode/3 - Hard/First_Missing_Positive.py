class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        singleValArr = set(nums)
        firstMissingVal = 1

        while firstMissingVal in singleValArr:
            firstMissingVal += 1
        
        return firstMissingVal
