class Solution:
    def minimumSum(self, num: int) -> int:
        
        arr = sorted([x for x in str(num)])
        
        frist_pairs = int(arr[0] + arr[2])
        second_pairs = int(arr[1] + arr[3])
        
        return frist_pairs + second_pairs
