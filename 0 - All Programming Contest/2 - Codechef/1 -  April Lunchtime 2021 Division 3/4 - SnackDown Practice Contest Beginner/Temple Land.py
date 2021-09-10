# problem link: https://www.codechef.com/SDPCB21/problems/TEMPLELA
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n % 2 == 0 or arr[0] != 1:
        print("no")

    else:

        mid = arr[n//2]
        result = 1
        for i in range(0, n//2):
            if arr[i]+1 == arr[i+1]:
                continue
            else:
                result = 0
                break


        for j in range(n//2, n-1):
            if arr[j]-1 == arr[j+1]:
                continue
            else:
                result = 0
                break

        if result == 1:
            print("yes")
        else:
            print("no")