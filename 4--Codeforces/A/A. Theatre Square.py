from math import ceil
def  Theatre_Square(n, m, a):
    _n = ceil(n / a)
    _m = ceil(m / a)
    """print(_n)
    print(_m)"""

    return _n * _m

if __name__ == '__main__':
    n, m, a = map(int, input().split())
    res = Theatre_Square(n, m, a)
    print(res)