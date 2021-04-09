class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            r = int(str(x)[::-1])
            if x == r:
                return True
