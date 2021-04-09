from collections import defaultdict


class Solution(object):
    def lonelyinteger(a):
        Counter = defaultdict(int)
        max_ = 101

        for i in a:
            Counter[i] += 1

        for Count in Counter:
            if Counter[Count] <= 1:
                return Count


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = Solution.lonelyinteger(a)

    print(str(result) + '\n')
