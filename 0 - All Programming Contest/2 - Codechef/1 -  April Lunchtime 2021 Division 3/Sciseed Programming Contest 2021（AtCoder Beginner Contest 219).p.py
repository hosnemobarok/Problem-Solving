
def A():
    num = int(input())
    n = 40
    i = 70
    a = 90
    if num >= 0 and num < n:
        res = n - num
        print(res)

    elif num >= 40 and num < i:
        res = i - num
        print(res)

    elif num >= 70 and num < a:
        res = a - num
        print(res)

    else:
        print("expert")
A()