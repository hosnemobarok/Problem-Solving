# problem link: https://www.codechef.com/YTPP001/problems/NUMPLIN
n = int(input())

if str(n) == str(n)[::-1]:
    print("YES")
else:
    print("NO")