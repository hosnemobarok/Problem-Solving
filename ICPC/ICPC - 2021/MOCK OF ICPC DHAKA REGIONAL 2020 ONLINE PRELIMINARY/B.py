if __name__ == '__main__':

    t = int(input())
    for i in range(t):

        size = int(input())
        li = list(map(int, input().split()))

        if size == 1:
            r = li[0] * li[0]
            res = 0

            for j in range(2, li[0]):
                if r % j != 0:
                    res = 0

                else:

                    print(j* (r % j))
                    res += 1

            if res == 0:
                print("Case %d: %d"%(i+1, r))
        else:
            _sort = sorted(li)
            mid = size // 2
            print("Case %d: %d"%(i+1, _sort[mid-1] * _sort[mid]))


