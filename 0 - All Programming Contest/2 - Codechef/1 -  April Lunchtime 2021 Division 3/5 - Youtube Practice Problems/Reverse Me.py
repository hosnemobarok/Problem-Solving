# problem link: https://www.codechef.com/YTPP001/problems/REVMEE

n = int(input())
arr = list(map(int, input().split()))
print(*arr[::-1])