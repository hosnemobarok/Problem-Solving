def recursion(lo, hi):
    if lo < hi:
        print(lo, end=' ')
        recursion(lo+1, hi)

    elif lo == hi:
        print(lo)

if __name__ == '__main__':
    for _ in range(int(input())):
        hi = int(input())
        recursion(1, hi)




# 2nd solution
def show(n):

    if(n>0):
            show(n-1)
            print(str(n),end=" ")


t = int(input())
for t in range(t):
    n = int(input())
    show(n)
    print()

