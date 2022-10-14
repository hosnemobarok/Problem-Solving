# problem link : https://toph.co/p/neat-brackets

def solution(str):
    stack = []

    for ch in str:

        if ch == "(":
            stack.append(ch)

        else:
            if not stack:
                return False

            last = stack.pop()

            if last == "(":
                if ch != ")":
                    return False

    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    s = input()
    if solution(s):
        print("Yes")
    else:
        print("No")
