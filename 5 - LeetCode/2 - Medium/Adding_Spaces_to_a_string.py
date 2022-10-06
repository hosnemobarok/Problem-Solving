# problem link : https://leetcode.com/problems/adding-spaces-to-a-string/description/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        # res = ""
        # count = 0

        # for ch in range(len(s)):
        #     if count == len(spaces):
        #         res += s[ch]
        #         continue

        #     else:
        #         l = spaces[count]

        #         if ch == l:
        #             res += " %s"%(s[ch])
        #             count += 1

        #         else:
        #             res += s[ch]

        # return res

        spaces = set(spaces)

        res = ""

        for ch in range(len(s)):
            if ch in spaces:
                res += " %s"%(s[ch])
            else:
                res += s[ch]
        return res
            
