from collections import Counter
def sockMerchant(n, ar):
    sum=0
    for values in Counter(ar).values():
        sum+=values//2
    return sum


if __name__=="__main__":
    n = input()
    arr = input().strip().split()
    print(sockMerchant(n, arr))
