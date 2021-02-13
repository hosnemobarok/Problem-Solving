class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num <= 1:
            return False

        sum = 1
        sqrt = int(num ** 0.5)

        for i in range(2, sqrt + 1):
            if num % i == 0:
                sum += (i + num // i)

        return sum == num