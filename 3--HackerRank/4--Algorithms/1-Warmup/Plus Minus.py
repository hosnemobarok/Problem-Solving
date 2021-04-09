def Plus_Minus(n, arr):
    positive, negative, zero = [], [], []
    for i in arr:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            zero.append(i)
    p_result = len(positive)/n
    n_result = len(negative)/n
    z_result = len(zero)/n
    print("%.6f"%p_result)
    print("%.6f"%n_result)
    print("%.6f"%z_result)
    exit()


if __name__=="__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(Plus_Minus(n, arr))
