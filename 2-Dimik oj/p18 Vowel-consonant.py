#Dimikoj Accept

T = int(input())
for i in range(T):
    vowels = "aeiouAEIOU"
    con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    v = ''
    c = ''
    string = input()
    for j in string:
        if j in vowels:
            v += j
        elif j in con:
            c += j
    print(v)
    print(c)