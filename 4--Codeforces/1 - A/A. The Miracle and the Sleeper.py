def solve():
    for _ in range(int(input())):
        l, r = map(int, input().split())

        mid = (r+1) // 2-1
        
        if mid + 1 >= l:
            print(mid)
        else:
            print(r % l)
            
solve()
        