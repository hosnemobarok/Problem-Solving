for _ in range(int(input())):
    string = input()
    stack = ['e']

    #################append###############

    for ch in string:
        if ch == '(':
            stack.append(ch)

        elif ch == '{':
            stack.append(ch)

        elif ch == "[":
            stack.append(ch)

        elif ch == "<":
            stack.append(ch)

        #################pop#####################

        if ch == ')':
            k = stack.pop()
            if k != '(':
                stack.append('')
                break

        elif ch == '}':
            k = stack.pop()
            if k != '{':
                stack.append('')
                break

        elif ch == ']':
            k = stack.pop()
            if k != '[':
                stack.append('')
                break

        elif ch == '>':
            k = stack.pop()

            if k != '<':
                stack.append(ch)
                break

    if stack == 0 or stack[len(stack) - 1] != 'e':
        print('NO')
    else:
        print("YES")




# 2nd solution
def Balanced_Brackets(s):
    stack = list()
    table = {")":"(", "]":"[", "}":"{"}

    for x in s:
        if stack and table.get(x) == stack[-1]:
            stack.pop()

        else:
            stack.append(x)

    if stack:
        return "NO"
    else:
        return "YES"


if __name__=="__main__":
    for _ in range(int(input())):
        s = input()
        print(Balanced_Brackets(s))
