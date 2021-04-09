def symmetric(n,m):
    for i in sorted(set(m) ^ set(n)):
        print(i)
    return exit()

if __name__=="__main__":
    M = int(input())
    m = map(int, input().split())
    N = int(input())
    n = map(int, input().split())
    print(symmetric(n,m))
