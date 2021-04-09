class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.islower() or i.isalnum():
                res += i.lower()

        return res == res[::-1]