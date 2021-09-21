def Solution():
    for _ in range(int(input())):
        string = input()
        res = string[::2] + string[-1]
        print(res)
# Drive Code
Solution()