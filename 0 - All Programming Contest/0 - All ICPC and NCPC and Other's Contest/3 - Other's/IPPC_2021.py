def Solution_C():
    s = input()

    r = set(s)
    if len(s) == len(r):
        print("YES")
    else:
        print("NO")


# Solve
def Solution_E():
    s = input()
    count = 0
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            count += 1

    if count > 2:
        print("YES")
    else:
        print("NO")


def Solution_F():
    for _ in range(int(input())):
        num = int(input())
        res = num * (num + 1) // 2
        print(res)


#Solution_C()
#Solution_E()
#Solution_F()