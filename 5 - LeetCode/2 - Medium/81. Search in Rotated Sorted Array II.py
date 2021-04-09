class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        rev = nums[::-1]
        s = sorted(rev)

        for i in range(0, len(s)):
            if nums[i] == target:
                return True

        return False