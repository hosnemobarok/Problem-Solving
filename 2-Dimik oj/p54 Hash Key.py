#Dimikoj

for T in range(int(input())):
    s1,s2 = input().split()
    a1,a2 = 1,1

    for ch1,ch2 in zip(s1,s2):
        a1 *= ord(ch1)
        a2 *= ord(ch2)
    if(a1%97)==(a2%97):print('YES')
    else:print("NO")