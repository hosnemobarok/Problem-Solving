# problem link : https://leetcode.com/problems/simplify-path/description/

class Solution(object):
    """
    def simplifyPath(self, path: str) -> str:

        res = ""
        dot = ""

        for i in path:
            if i == ".":
                dot += i

            else:
                if i == "/":
                    if len(res) > 0:
                        if res[-1] == "/":
                            continue
                        else:
                            res += i
                if i != "/":
                    res += i
                if len(dot) <= 2:
                    dot = ""
                if len(dot) >= 3:
                    res += dot
                    dot = ""

        result = "/"+res+dot if len(dot) >= 3 else "/"+res
        n = len(result)

        if n == 1: return result
        if n > 0 and result[-1] == "/": return result[:-1]
        else: return result
    """

    def simplifyPath(self, path):

        arr = path.split("/")
        res = []

        for i in arr:
            if i == "..":
                if len(res) > 0:
                    res.pop()

            elif i != "." and len(i) > 0:
                res.append(i)

        return "/"+"/".join(res)

