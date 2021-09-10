# problem link: https://www.codechef.com/YTPP001/problems/FINDMELI
n, t = map(int, input().split())
arr = list(map(int, input().split()))

if t in arr:
    print(1)
else:
    print(-1)