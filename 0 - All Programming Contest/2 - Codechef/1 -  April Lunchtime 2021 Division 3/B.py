for _ in range(int(input())):
    str_size, b_point, g_point = map(int, input().split())

    b_count = 0
    g_count = 0
    counter = "EQUINOX"

    for i in range(str_size):
        string = input()
        if string[0] in counter:
            b_count += b_point
        else:
            g_count += g_point

    if b_count == g_count:
        print("DRAW")

    elif g_count > b_count:
        print("ANURADHA")
    else:print("SARTHAK")



