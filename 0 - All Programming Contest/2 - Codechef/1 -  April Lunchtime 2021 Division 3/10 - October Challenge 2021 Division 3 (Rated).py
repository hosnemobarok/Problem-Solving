# def aSolution():
#     for _ in range(int(input())):
#         a, b = map(int, input().split())
#         if a > 0 and b > 0:
#             print("Solution")
#         elif a == 0:
#             print("Liquid")
#         else:
#             print("Solid")
#
# aSolution()

# def bSolution():
#     for _ in range(int(input())):
#         a, b, c, d = map(int, input().split())
#         if (a+b) <= d and d < (a+b+c):
#             print(2)
#         elif a<= d and (a+b) > d:
#             print(3)
#         else:
#             print(1)
#
# bSolution()

# def subSet(n):
#     res = 0
#     while n > 0:
#         res += 1
#         n >>= 1
#     return res
#
# def cSolution():
#     for _ in range(int(input())):
#         N = int(input())
#         n = subSet(N)
#
#         a = N - pow(2, n-1) + 1
#         b = pow(2, n-1) - pow(2, n-2)
#         result = max(a, b)
#         print(result)
#
# cSolution()


# def dSolution():
#     for _ in range(int(input())):
#         n = int(input())
#         res = 1
#         if n == 0:
#             print(1)
#         elif n == 1 or n == 2:
#             print(2)
#         else:
#             while res*2 <= n:
#                 res *= 2
#
#             if res == n:
#                 print(n)
#
#             elif n == (2*res-1):
#                 print(n+1)
#             else:
#                 print(res)
# dSolution()
