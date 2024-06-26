class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = dic[s[0]]
        lastChar = s[0]

        for char in s[1:]:
            
            if dic[lastChar] >= dic[char]:
                res += dic[char]
                lastChar = char

            else:
                minus = dic[char] - dic[lastChar]
                res -= dic[lastChar]
                res += minus
                lastChar = char

        return res
