class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        if len(columnTitle) == 0:
            return -1

        sum = 0
        for ch in columnTitle:
            sum = sum * 26 + ord(ch) - ord("A") + 1

        return sum
