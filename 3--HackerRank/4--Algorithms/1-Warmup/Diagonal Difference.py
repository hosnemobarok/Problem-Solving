if __name__=="__main__":
    n = int(input())
    r1,r2 = 0,0
    for i in range(0, n):
        a = input().split()

        r1 += int(a[i])

        r2 += int(a[n-i-1])
    print(abs(r1-r2))
