from collections import *
for _ in range(int(input())):
    size = int(input())
    arr = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    
    res = float("inf")
    arr.sort()
    arr1.sort()
    
    m = defaultdict(int)
    for k in range(size-1):
        a = arr1[k] - arr[k]
        b = arr1[k] - arr[k+1]
        
        if a != b:
            if a > 0:
                m[a] += 1 
            if b > 0:
                m[b] += 1 
        
        else:
            if a > 0:
                m[a] += 1 
    for i in m.keys():
        if m[i] == size - 1:
            res = min(res, i)
    print(res)
            
                
                
                
                
                
                
        
    