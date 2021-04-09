class Solution:
    def maxPower(self, s: str) -> int:

        l_c = []
        count = 0

        for i in range(len(s) - 1):

            if s[i] == s[i + 1]:
                count += 1

                l_c.append(count)

            else:
                count = 0

        if l_c == []:
            return 1

        else:
            return max(l_c) + 1