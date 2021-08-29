for _ in range(int(input())):
    N, K, S = map(int, input().split())
    
    s = (S - (N*N))
    print(s//(K-1))