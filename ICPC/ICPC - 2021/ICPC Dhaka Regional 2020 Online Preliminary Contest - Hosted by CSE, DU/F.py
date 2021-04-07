from math import gcd as bltin_gcd


def coprime2(a, b):
    return bltin_gcd(a, b) == 1


def solution():
    t = int(input())
    for index in range(1, t + 1):
        ans = 0
        a, b, m = list(map(int, input().split()))
        for i in range(0, m + 1):
            if coprime2(a + i, b + i):
                ans += 1

        print("Case {}: {}".format(index, ans))


solution()




#2nd niom

def __gcd(a, b):

    if a == 0 or b == 0: return 0
    if a == b: return a

    if a > b:
        return __gcd(a - b, b)

    return __gcd(a, b - a)



def coprime(a, b):
    return __gcd(a, b) == 1


if __name__ == '__main__':
    t = int(input())
    for index in range(1, t+1):
        ans = 0

        a, b, m = list(map(int, input().split()))

        for i in range(0, m + 1):

            if coprime(a+i, b+i):

                ans += 1

        print("Case {}: {}".format(index, ans))
