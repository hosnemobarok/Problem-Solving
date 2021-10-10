# problem link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return len(nums) != len(temp)
