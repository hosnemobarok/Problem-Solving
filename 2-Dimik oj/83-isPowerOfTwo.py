# Accept

def isPowerOfTwo(n):
    if (n == 0):
        return False

    while (n != 1):
        if (n % 2 != 0):
            return False

        n = n // 2

    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        if isPowerOfTwo(n):
            print("It's a power of 2")
        else:
            print("Not a power of 2")
