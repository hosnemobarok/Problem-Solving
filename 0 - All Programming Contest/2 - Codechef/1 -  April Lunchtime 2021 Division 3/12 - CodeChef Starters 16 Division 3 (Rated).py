# contest link: https://www.codechef.com/START16C/

#for _ in range(int(input())):
#    n, x, p = map(int, input().split())
#
#    Sum = 3*x - (n-x)
#
#    if p <= Sum:
#        print("PASS")
#    else:
#        print("FAIL")


#T = int(input())
#for case in range(T):
#    x, y = map(int, input().split())
#    st = input()
#
#    total = 0
#    totalDay = 0
#    res = 0
#
#    for i in range(0, 30):
#        if st[i] == "1":
#            res += x
#            total += 1
#
#        else:
#            bigDay = max(totalDay, total)
#            total = 0
#
#    r = max(total, totalDay)
#    res += r * y
#    print(res)


#for _ in range(int(input())):
#    n = int(input())
#    st = input()
#
#    res = 0
#
#    for i in range(0, n-1):
#        if st[i] == "L" and st[i+1] == "L":
#            print("YES")
#
#        elif st[i] == "R" and st[i+1] == "R":
#            print("YES")
#    else:
#        print("NO")
