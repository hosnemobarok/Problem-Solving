#Dimikoj Accept

for T in range(int(input())):
    s = input()
    r = ''
    for i in range(len(s)):
        if s[i] in 'L':
            r +=s[i-1]
        elif s[i] in 'R':
            r +=s[i+1]
        else:
            r +=s[i]
    print(r)



#Runtime Error

for T in range(int(input())):
    string = input()
    for i in string:
        ind = string.index(i)
        if i == 'L':
            string = string.replace(i, string[ind-1])
        elif i == 'R':
            string = string.replace(i, string[ind+1])
    print(string)
