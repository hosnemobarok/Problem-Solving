def Birthday_Cake_Candles(arr):
    resutl = arr.count(max(arr))
    return resutl

if __name__=="__main__":
    n = int(input())
    N = list(map(int, input().split()))
    print(Birthday_Cake_Candles(N))
