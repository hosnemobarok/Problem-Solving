
def solve(x, y, z):

    if x == y and y == z:
        return "Equilateral Triangle"

    elif x == y or x == z or y == z:
        return "Isosceles Triangle"
    else:
        return "Bad Triangle"


if __name__ == '__main__':
    x, y, z = map(int, input().split())
    res = solve(x, y, z)
    print(res)