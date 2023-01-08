# contest link : https://vjudge.net/contest/537392#problem

def b_Solution():
    n = int(input())
    print(chr(n))

def d_Solution():
    n = int(input())

    print(str(n)[-2:])

def c_Solution():
    a, b, c = map(int, input().split())
    li = sorted([a, b, c])
    if li[1] == b:
        print("Yes")
    else:
        print("No")

import math
def s_Solution():
    t = int(input())
    for case in range(t):
        n = int(input())
        res = int(math.sqrt(n))
        print(res)

def r_Solution():
    car_size = int(input())
    total_student_arr = list(map(int, input().split()))
    total_student = sum(total_student_arr)

    count = 0
    while total_student >= 5:
        count += 1
        total_student -= 5

    if total_student > 0 and total_student != 0:
        print(count+1)
    else:
        print(count)


def g_helper(n, r):
    start = 1
    if r > n - r:
        r = n - r
    for i in range(0, r):
        start = start * (n - i)
        start = start // (i + 1)
    return start

def g_Solution():
    n = int(input())
    for i in range(0, n):
        for j in range(0, i + 1):
            print(g_helper(i, j), end=" ")
        print()

def i_Solution():
    s = input()
    a = s[1:]
    b = a[:-1]
    res = s[0]+str(len(b))+s[-1]
    print(res)

def l_Solution():
    point = [5, 4, 3, 2, 1]
    n = int(input())
    res = 0
    for i in range(len(point)):
        res += n//point[i]
        n %= point[i]
    print(res)


def v_Solution():
    t = int(input())
    print("\n")
    for case in range(1, t+1):
        n = int(input())
        arr = list(map(int, input().split()))

        sum = 0
        for x in arr:
            if (x > 0):
                sum += x

        print("Case %d: %d\n" % (case, sum))
"""
#include <stdio.h>
    int main() {
        int T,N;
        scanf("%d\n",&T);

        int i,j,dust;
        unsigned long long int sum = 0;
        for(i =0; i<T;i++) {
            scanf("%d",&N);
            for(j=0;j<N;j++)
            {
                scanf("\n%d",&dust);
                if(dust>0)
                sum+=dust;
            }
            printf("Case %d: %lld\n",i+1,sum);
            sum =0;
        }
        return 0;
    }
"""

def k_Solution():
    n = int(input())
    print(25)

def m_Solution():
    n = int(input())
    res = "YES" if (n % 2 == 0) and n > 2 else "NO"
    print(res)

def j_Solution():
    n = int(input())

    arr = []
    for i in range(n):
        arr.append(2 ** i)

    for i in range(1, 8):
        if arr[-i] <= n:
            print(arr[-i])
            break

def n_Solution():
    while True:
        try:
            a, b = map(int, input().split())
            print(abs(a - b))
        except EOFError:
            break

def t_Solution():
    x, y, n = map(int, input().split())
    for i in range(1, n+1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")
        elif i % y == 0:
            print("Buzz")

        elif i % x == 0:
            print("Fizz")
        else:
            print(i)

def o_Solution(): # ac
    n = int(input())
    li = map(int, input().split())

    min_value = 11111
    max_value = -1

    res = -2

    for i in li:
        if i < min_value:
            min_value = i
            res += 1

        if i > max_value:
            max_value = i
            res += 1

    print(res)

def o_Solution(): # not ac
    n = int(input())
    li = list(map(int, input().split()))

    result = 0
    for i in range(n-1):
        if li[i+1] > li[i]:
            result += 1
    print(result)

def e_Solution():
    r, c = map(int, input().split())
    arr = []

    for i in range(2):
        li = list(map(int, input().split()))
        arr.append(li)

    r = r - 1
    c = c - 1
    print(arr[r][c])

def p_Solution():
    n = int(input())
    res = n*(n+1)//2
    print(res-(n-1))


def f_Solution():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            if i % 2 == 0:
                r = n*b
                res = ""
                for k in range(r//b):
                    if len(res) < r:
                        res += "."*b
                        if n > 1:
                            if len(res) < r:
                                res += "#"*b
                print(res)

            else:
                r = n * b
                res = ""
                for k in range(r // b):
                    if len(res) < r:
                        res += "#" * b
                        if n > 1:
                            if len(res) < r:
                                res += "." * b
                print(res)

def h_Solution():
    for i in range(1, 10):
        for j in range(1, 10):
            print("%dx%d=%d"%(i, j, i*j))

# b_Solution()
# d_Solution()
# c_Solution()
# s_Solution()
# r_Solution()
# g_Solution()
# i_Solution()
# l_Solution()
# v_Solution()
# k_Solution()
# m_Solution()
# j_Solution()
# n_Solution()
# t_Solution()
# o_Solution()
# e_Solution()
# p_Solution()
# f_Solution()
# h_Solution()
