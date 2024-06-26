class Solution:

    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:
            if i in "({[":
                stack.append(i)
            
            else:
                if stack == []:
                    return False
                
                else:

                    lastChar = stack[-1]

                    if lastChar == "(":
                        if i == ")":
                            stack.pop()
                        else:
                            return False
                    
                    elif lastChar == "{":
                        if i == "}":
                            stack.pop()
                        else:
                            return False

                    elif lastChar == "[":
                        if i == "]":
                            stack.pop()
                        else:
                            return False

        return (len(stack) == 0)
