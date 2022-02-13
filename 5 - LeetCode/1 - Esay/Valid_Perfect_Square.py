class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num**0.5)**2 == int(num)
    
    
# TLE code
#         if num == 1: return True
#         flag=0
#         for i in range(1,num):
#             if num==i*i:
#                 return True
#                 flag=1
#                 break
#         if flag==1:
#             pass
#         else:
#             return False