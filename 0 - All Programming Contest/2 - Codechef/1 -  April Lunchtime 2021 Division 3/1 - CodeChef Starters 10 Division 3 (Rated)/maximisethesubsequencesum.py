# Accept
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    for i in range(k):
        if arr[i] < 0:
            arr[i] = arr[i]*(-1)
        else:
            break
    
    s = 0
    for i in range(n):
        if arr[i] > 0:
            s += arr[i]
            
    print(s)

"""
# Runtime Error
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if len(set(arr)) == 1:
        print(0)
    elif sorted(arr) == arr:
        print(sum(arr))
    else:
        res = []
        p = 0
        for i in range(len(arr)):
            if arr[i] < 0:
                res.append(abs(arr[i]))
                
            else:
                p += arr[i]
                
        res.remove(min(res))
        print(p + sum(res))
"""