def is_Prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    # 2 skip all even number is'n prime.
    if n > 2 and n % 2 == 0:
        return False

    root = int((n ** 0.5))

    for i in range(3, root+1, 2):
        if n % i == 0:
            return False

    return True

# Driver Code
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        res = is_Prime(n)
        if res:
            print("%d is a prime"%n)
        else:
            print("%d is not a prime" % n)
