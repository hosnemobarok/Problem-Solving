class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ln = len(nums)
        ls = set(nums)
        li = list(ls)

        
        sor = sorted(nums)

        if ln == 1 or len(ls) == 1: return nums[0]
        elif ln == 2 or len(ls) == 2: return sor[-1]
        elif ln == 3 or len(ls) == 3: return sor[0]
        else:
            for i in range(2):

                m = max(li)
                li.remove(m)

            return max(li)