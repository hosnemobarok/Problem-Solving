"""
problem name: visiting house
Solution formula:

    example - axeb
            a -> x = 1 -> 24
            1 - 24 = 23
            26 - 23 = 3
            total way = [23, 3] min - 3

            x -> e = 24 -> 5
            24 - 5 = 19
            26 - 19 = 7
            total way = [19, 7] min - 7

            e -> b = 5 -> 2
            5 - 2 = 3
            26 - 3 = 23
            total way = [3, 23] min - 3

            result = 3+7+3
"""

def convert(ch):
    up = ch.upper()
    return ord(up) - 64


def solution(st):
    n = len(st)

    count = 0
    for i in range(1, n):
        a = convert(st[i - 1])
        b = convert(st[i])

        x = abs(a - b)
        y = abs(26 - x)
        second = min(sorted([x, y]))

        count += second

    print(count)

solution("axeb")
