#Dimikoj Accept

T = int(input())
for i in range(T):
    T = input()
    word = T.split()
    for j in word:
        if j == ' ':
            continue
    T = (len(word))
    print(T)



#2nd niom
num = input()
for w in range(int(num)):
    num2 = input().split()
    print(len(num2))