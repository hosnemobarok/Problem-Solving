class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
            else:
                return i