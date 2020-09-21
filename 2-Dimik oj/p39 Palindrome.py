#Dimikoj Accept

T = int(input())
for i in range(T):
    S = input()
    R = S[::-1]
    if S == R:
        print("Yes! It is Palindrome!")
    else:
        print("Sorry! It is not Palindrome!")