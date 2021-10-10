# problem link: https://codeforces.com/contest/937/problem/A

def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    s = set(nums)
    if 0 not in s:
        print(len(s))
    else:
        s.remove(0)
        print(len(s))

solution()
