# problem link: https://codeforces.com/problemset/problem/431/A
def Solution():
    a, b, c, d = map(int, input().split())
    numString = input()

    sum = 0
    for i in numString:
        if i == "1":
            sum += a
        elif i == "2":
            sum += b
        elif i == "3":
            sum += c
        elif i == "4":
            sum += d

    print(sum)


Solution()