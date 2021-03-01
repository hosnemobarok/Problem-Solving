def solve(n):
    haf = n // 2
    print(haf)

    if n % 2 == 0:
        return "2 "*haf
    else:
        return "2 "*(haf-1)+"3"


if __name__ == '__main__':
    n = int(input())
    res = solve(n)
    print(res)