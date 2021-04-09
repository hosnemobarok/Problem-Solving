class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = [str(i) for i in digits]
        plus_one = str(int(''.join(d))+1)
        return [x for x in plus_one]