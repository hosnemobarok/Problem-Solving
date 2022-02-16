class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul_sum = 1
        add_sum = 0
        
        while n > 0:
            digit = n % 10
            n //= 10
            mul_sum *= digit
            add_sum += digit
        
        return mul_sum - add_sum
