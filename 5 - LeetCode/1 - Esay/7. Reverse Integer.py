class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            x=int(str(x)[::-1])
        else:
            x=-int(str(-x)[::-1])
        return x if x<=(2**31-1) and x>=-(2**31) else 0