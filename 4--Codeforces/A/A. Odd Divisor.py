def Odd_Divisor(num):

    while num % 2 == 0:
        num //= 2

    if num < 2:
        return "NO"

    return 'YES'

if __name__=="__main__":
    for _ in range(int(input())):
        num = int(input())
        res = Odd_Divisor(num)
        print(res)