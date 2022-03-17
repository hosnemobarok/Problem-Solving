def isPalindrome(num):

    temp = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return temp == rev

for case in range(int(input())):
    n = int(input())
        
    n += 1

    while True:
        if isPalindrome(n):
            break
        n += 1
        
    print(n)

