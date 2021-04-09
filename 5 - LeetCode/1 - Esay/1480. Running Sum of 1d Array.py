class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = []

        result = []

        for i in nums:
            s.append(i)
            result.append(sum(s))
        return result