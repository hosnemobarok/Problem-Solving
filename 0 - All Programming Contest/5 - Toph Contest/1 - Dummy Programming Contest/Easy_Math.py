while 1:
    a, b, m = map(int, input().split())
    if a + b + m == 0:break
    print(pow(a, b, m))
