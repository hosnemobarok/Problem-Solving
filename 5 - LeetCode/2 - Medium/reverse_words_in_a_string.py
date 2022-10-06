# problem link : https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""

        for i in s.split()[::-1]:
            res += i
            res += " "

        return res.rstrip()
