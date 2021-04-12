
size = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ff = b[:1]
l = b[:-1]
ll = b[-1:]
bb = ll + l[1:] + ff


res = 0
for i in range(size):
    val = a[i] - bb[i]
    res += abs(val)


print(res)
