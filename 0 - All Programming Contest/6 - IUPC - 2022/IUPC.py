# problem link: https://algo.codemarshal.org/contests/aust-2022/problems/G

def Solution():
    test_case = int(input())
    for case in range(1, test_case + 1):

        prime_number = [2, 3, 5, 7, 11, 13, 17, 19]
        size = int(input())
        prime_num = list(map(int, input().split()))

        isPrime = True
        for i in prime_num:
            if i in prime_number:
                isPrime = True
            else:
                isPrime = False
                break
        if isPrime:
            print("Case %d: Yes" % (case))
        else:
            print("Case %d: No" % (case))


Solution()
