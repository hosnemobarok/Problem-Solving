# problem link: https://www.codechef.com/YTPP001/problems/RNGEODD
l, r = map(int, input().split())

for i in range(l, r+1):
    if i % 2 == 1:
        print(i, end=" ")