def compareTriplets(a,b):
    A = (a[0]>b[0]) + (a[1]>b[1]) + (a[2]>b[2])
    B = (a[0]<b[0]) + (a[1]<b[1]) + (a[2]<b[2])
    print(A,B)
    exit()


if __name__=="__main__":
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(compareTriplets(a,b))
