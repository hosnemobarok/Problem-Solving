# contest link: https://atcoder.jp/contests/abc223
def aSolution():
    n = int(input())
    s = str(n)[::-1]
    a = s[:2]

    if len(a) == 2 and a.count("0") == 2:
        print("Yes")
    else:
        print("No")



def bSolution():
    pass


bSolution()
