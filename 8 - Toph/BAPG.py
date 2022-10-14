# problem link : https://toph.co/p/bapg

def solution():
    t = int(input())
    for case in range(1, t+1):

        n, m = map(int, input().split())
        arr = list(map(int, input().split()))

        arr.sort()
        print(sum(arr[-n:]))

solution()
