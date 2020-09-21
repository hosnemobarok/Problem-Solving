#Dimikoj NOt Accept cesta korte hobe

T = int(input())
for i in range(T):
    N = int(input())
    if N > 1:
        for j in range(2,N):
            if N % j == 0:
                print("%d is not a prime"%N)
                break
        else:
            print("%d is a prime"%N)



#2nd Niom Dimikoj Accept
T = int(input())
for i in range(T):
    N = int(input())
    if N == 2:
        print("%d is a prime" % (N))
    else:
        a = []
        z = int(N ** (1 / 2))
        for f in range(2, z + 1):
            if N % f == 0:
                a.append(True)

        if any(a):
            print("%d is not a prime" % (N))
        else:
            print("%d is a prime" % (N))



#3rd niom helal vi Dimikoj Accept
def prime(num):
    import math
    if num == 2:
        return True
    if num%2 == 0:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num = int(input())
        if prime(num):
            print("%d is a prime"%num)
        else:
            print("%d is not a prime"%num)