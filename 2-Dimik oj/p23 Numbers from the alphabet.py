print(''.join(str(ord(i)-64) for i in input()))

#Dimikoj Accept

for i in range(int(input())):print(''.join(str(ord(ch)-64) for ch in input()))

#2nd Rules
for T in range(int(input())):
    t = input()
    for ch in t:
        print(ord(ch) - 64, end='')
    print()
