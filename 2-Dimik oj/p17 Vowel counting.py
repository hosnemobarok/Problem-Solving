#Dimikoj Accept

T = int(input())
for i in range(T):
    vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    S = input()
    count = 0
    for j in S:
        if j in vowel:
            count += 1
    print('Number of vowels =',count)