# ac
arr = []
for _ in range(int(input())):
    li = []
    s, t = input().split()
    li.append(s)
    li.append(t)
    arr.append(li)

count = 0
for i in range(1, len(arr)):

    f = arr[0]
    if arr[i] == f:
        print("Yes")
        break
else:
    print("No")
