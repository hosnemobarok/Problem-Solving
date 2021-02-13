'''
    Time Complexity     : O(n)
    Space Complexity    : O(1)
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        current_index = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[current_index] = nums[i]

                current_index += 1

        return current_index




