class Solution:
    def isValid(self, s: str) -> bool:
        table = {')': '(', ']': '[', '}': '{'}
        stack = []
        for x in s:
            if stack and table.get(x) == stack[-1]:
                stack.pop()
            else:
                stack.append(x)

        if stack:
            return False
        else:
            return True