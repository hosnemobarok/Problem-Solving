class Solve:
    def fibonacciModified(self, t0, t1, n):
        fibs = {1: t0, 2: t1}

        for i in range(3, n + 1):
            add = t0 + t1 ** 2
            fibs[i] = add
            t0, t1 = t1, add

        return fibs[n]


if __name__ == "__main__":
    t0, t1, n = list(map(int, input().split()))
    solve = Solve()
    res = solve.fibonacciModified(t0, t1, n)
    print(res)
