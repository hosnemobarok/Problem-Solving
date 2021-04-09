class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check_ari(ary):
            N = len(ary)
            diff = ary[1] - ary[0]
            return all(ary[i] - ary[i - 1] == diff for i in range(2, N))

        return [check_ari(sorted(nums[s:e + 1])) for s, e in zip(l, r)]