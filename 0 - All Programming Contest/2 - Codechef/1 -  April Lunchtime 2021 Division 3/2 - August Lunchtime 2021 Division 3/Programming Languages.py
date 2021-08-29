for _ in range(int(input())):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    a = sorted([A1, B1])
    b = sorted([A2, B2])

    c = sorted([A, B])
    if c == a:
        print(1)

    elif c == b:
        print(2)

    else:
        print(0)

