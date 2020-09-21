for i in range(int(input())):

    a, b, c = map(float, input().split())
    res = (a*2 + b*3 + c*5) / 10
    print('%.1f'%(res))