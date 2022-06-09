class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # time complexity vely long O(n)
        
        # for i in range(len(numbers)):
        #     for j in range(i, len(numbers)):
        #         if (numbers[i] + numbers[j]) == target:
        #             return [i+1, j+1]
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            
            two_val_sum = numbers[left] + numbers[right]
            
            if two_val_sum == target:
                return [left+1, right+1]
            
            elif two_val_sum < target:
                left += 1
            else:
                right -= 1
