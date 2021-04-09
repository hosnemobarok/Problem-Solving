class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rote = nums[::-1]
        s = sorted(rote)

        for i in range(len(s)):
            if nums[i] == target:
                return i
        return -1