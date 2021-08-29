for _ in range(int(input())):
    A, B, C = map(int, input().split())
    arr = [A, B, C]
    mi = min([A, B, C])
    
    if arr.index(mi) == 0:
        print("Draw")
    elif arr.index(mi) == 1:
        print("Bob")
    else:
        print("Alice")