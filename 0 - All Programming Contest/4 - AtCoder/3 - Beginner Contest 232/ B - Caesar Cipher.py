# contest link: https://atcoder.jp/contests/abc232
# not accept

s = input()
t = input()
if (s == "z" and t == "a") or s == t:
    print("Yes")

else:
    count = 0
    for i in range(len(s)):
        if ord(s[i]) < ord(t[i]):

            check = ord(s[0]) - ord(t[0])

            val = ord(s[i]) - ord(t[i])
            if check == val:
                count = 0
            else:
                count = 1
        else:
            count = 1

    if count == 0:
        print("Yes")
    else:
        print("No")