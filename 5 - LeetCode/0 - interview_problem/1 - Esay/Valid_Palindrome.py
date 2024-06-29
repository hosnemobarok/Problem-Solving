# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == "":
            return true

        convertString = ""

        for i in s:
            lower = i.lower()
            if ord(lower) >= 97 and ord(lower) <= 122 or lower in "0123456789":
                convertString += i.lower()

        return convertString == convertString[::-1]
