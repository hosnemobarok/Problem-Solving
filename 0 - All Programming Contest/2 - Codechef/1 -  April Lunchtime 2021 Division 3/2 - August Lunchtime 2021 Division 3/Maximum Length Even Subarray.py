def B():
    for _ in range(int(input())):
        size = int(input())
        res = (size*(size+1)) // 2

        if res%2==0:
            print(size)
        else:
            print(size-1)
B()