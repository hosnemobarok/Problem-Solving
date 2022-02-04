class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        first = -1
        last = -1
        for i in range(len(nums)) :
            if (target != nums[i]) :
                continue
            if (first == -1) :
                first = i
            last = i

        if (first != -1) :
            return [first, last]
        else:
            return [-1, -1]