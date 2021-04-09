class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i

            else:

                if nums[i] > target:
                    nums.insert(i, target)
                    nums.index(target)

        else:
            nums.append(target)
            return nums.index(target)

