def even_or_odd_sum(n):
    if n % 2 == 0:
        nn = (2 + n) // 2
        res1 = nn * (n - 1)

    if n % 2 != 0:
        a = 1
        l = n
        res2 = n * n * 2

    res = res1 + res2
    return res


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        res = even_or_odd_sum(n)
        print(res)
