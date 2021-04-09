def Arrys(A):
    print(*A[::-1])
    exit()


if __name__=="__main__":
    for N in range(int(input())):
        A = list(map(int, input().split()))
        print(Arrys(A))
