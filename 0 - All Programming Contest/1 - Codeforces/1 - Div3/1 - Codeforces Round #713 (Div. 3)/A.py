for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    s = list(set(arr))

    a, b = s[0], s[1]

    if arr.count(a) > arr.count(b):
        print(arr.index(b)+1)
    else:
        print(arr.index(a)+1)

"""
from collections import Counter
def singleNumber(arr):
    f = Counter(arr)

    for i in f:
        if (f[i] == 1):
            return arr.index(i)+1

if __name__ == '__main__':

    for _ in range(int(input())):
        size = int(input())
        arr = list(map(int, input().split()))
        print(singleNumber(arr))


# 2nd solution
from collections import Counter

for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))

    for k,v in Counter(arr).items():
        if v == 1:
            print(arr.index(k)+1)



# 3rd solution

te = int(input())
for test in range(te):
    n = int(input())
    l = list(map(int,input().split()))

    for i in range(len(l)):
        if l.count(l[i])==1:
            print(i+1)



# best solution
li = [2, 2, 10, 2, 2]

solv = 0

for i in li:
    solv ^= i

print(solv)
"""