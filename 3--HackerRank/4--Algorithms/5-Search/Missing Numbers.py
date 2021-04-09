class Solution:

    def missingNumbers(self, arr, brr):
        a = sorted(arr)
        b = sorted(brr)

        missing = []
        while a != [] and b!=[]:
            if a[0] == b[0]:
                a.pop(0)
                b.pop(0)

            else:
                missing.append(b.pop(0))

        missing = sorted(set(missing + b))

        return ' '.join(str(x) for x in missing)


if __name__ == '__main__':
    op = Solution()

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    m = int(input())
    brr = list(map(int, input().rstrip().split()))

    result = op.missingNumbers(arr, brr)
    print(result)
