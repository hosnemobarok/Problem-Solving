prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 0]

n, m = map(int, input().split())
if n not in prime or m not in prime:
    print("NO")
elif  n > m:
    print('NO')

else:

    ind1 = prime.index(n)
    ind2 = prime.index(m)

    if ind1 + 1 == ind2:
        print("YES")
    else:
        print("NO")
