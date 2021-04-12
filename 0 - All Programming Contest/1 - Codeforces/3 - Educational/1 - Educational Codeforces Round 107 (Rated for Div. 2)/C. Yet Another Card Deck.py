# Accept

p, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:

    ind = a.index(i)
    print(ind + 1, end=" ")

    a.remove(i)
    a.insert(0, i)



