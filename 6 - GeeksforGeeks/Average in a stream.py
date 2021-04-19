class Solution:
    def streamAvg(self, arr, n):
        # code here
        if len(arr) > 0:

            res = []
            res.append(arr[0] / 1)

            for i in range(2, len(arr) + 1):
                ind = arr[:i]

                k = sum(ind) / i
                res.append(k)

            return res


"""
li = [10, 20, 30, 40, 50]

if len(li) > 0:

    res = []
    res.append("%.2f"%(li[0] / 1))

    for i in range(2, len(li)+1):

        ind = li[:i]

        k = ("%.2f"%(sum(ind) / i))
        res.append(k)

    print(*res)
"""
