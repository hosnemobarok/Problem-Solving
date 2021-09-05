for _ in range(int(input())):
    size = int(input())
    s = input()

    if "U" in s:
        print(s.replace("U", "D"))

    else:
        print(s.replace("D", "U"))
