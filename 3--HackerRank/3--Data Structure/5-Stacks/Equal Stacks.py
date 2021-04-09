class Solution:

    def Equal_Stack(self, h1, h2, h3):
        l1, l2, l3 = 0, 0, 0

        for each in h1:
            l1 += each

        for each in h2:
            l2 += each

        for each in h3:
            l3 += each


        while (l1 != 0 and l2 !=0 and l3 !=0) and (l1 != l2 or l2 != l3):
            if max(l1, l2, l3) == l1:
                l1 -= h1[0]
                h1.pop(0)

            elif max(l1, l2, l3) == l2:
                l2 -= h2[0]
                h2.pop(0)

            else:
                l3 -= h3[0]
                h3.pop(0)

        if l1 == l2 and l2 == l3:
            return l1
        return 0


if __name__ == '__main__':
    op = Solution()
    n1, n2, n3 = map(int, input().split())

    h1 = list(map(int, input().split()))
    h2 = list(map(int, input().split()))
    h3 = list(map(int, input().split()))

    print(op.Equal_Stack(h1, h2, h3))
