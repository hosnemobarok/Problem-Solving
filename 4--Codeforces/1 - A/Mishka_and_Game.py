# problem link: https://codeforces.com/problemset/problem/703/A
def Solution():
    mTotal = 0
    cTotal = 0
    for _ in range(int(input())):
        m, c = map(int, input().split())
        if m > c:
            mTotal += 1
        elif m < c:
            cTotal += 1

    if mTotal > cTotal:
        print("Mishka")
    elif mTotal < cTotal:
        print("Chris")
    else:
        print("Friendship is magic!^^")

Solution()