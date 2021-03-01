def solve(a, b, c):
    aa = a + b + c
    bb = a * b * c

    cc = a + b * c
    dd = a * b + c

    ee = (a + b) * c
    ff = a * (b + c)


    li = [aa, bb, cc, dd, ee, ff]
    return max(li)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    res = solve(a, b, c)
    print(res)