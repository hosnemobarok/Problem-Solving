# Solve
while True:
    try:
        size = int(input())
        arr = list(map(int, input().split()))
        print(sum(arr))

    except EOFError:
        break
