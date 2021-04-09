if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    res = [0] * n
    j = 0
    for i in range(d, n):
        res[j] = a[i]
        j += 1

    i = 0
    for k in range(j, n):
        res[k] = a[i]
        i += 1

    for i in range(n):
        if i != n:
            print(res[i], end=' ')
        else:
            print(res[i])
