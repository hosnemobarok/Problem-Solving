class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 3:
            return nums

        odd = []
        even = []

        for index, value in enumerate(nums):
            if index % 2 == 1:
                odd.append(value)
            else:
                even.append(value)

        even.sort()
        odd.sort(reverse=True)

        res = []

        for index, value in enumerate(nums):
            if index % 2 == 0:
                res.append(even.pop(0))
            else:
                res.append(odd.pop(0))
        return res