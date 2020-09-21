#Dimikoj Accept

T = int(input())
for i in range(T):
    l = 'abcdefghijklmnopqrstuvwxyz'

    s = input()
    for cha in l:
        if cha in s:
            print('%s = %d'%(cha, s.count(cha)))
    if(i<T-1):
        print()