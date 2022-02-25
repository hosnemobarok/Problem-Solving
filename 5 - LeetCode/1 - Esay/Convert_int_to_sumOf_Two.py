class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if "0" in str(i) or "0" in str(n-i):
                continue
            return [i, n-i]