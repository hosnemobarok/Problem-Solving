
def Solve():

    n, m = map(int, input().split())

    arr = []
    k = "YES"
    for i in range(m):
        arr.append(list(map(int, input().split())))


    arr.sort()

    for i in arr:


        if i[0] < n:
            n += i[1]

        else:
            k = "NO"
            break

    print(k)



Solve()