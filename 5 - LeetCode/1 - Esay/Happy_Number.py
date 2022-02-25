"""
	Input: n = 19
	Output: true
	
	Explanation:
	12 + 92 = 82
	82 + 22 = 68
	62 + 82 = 100
	12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        temp = { n }
        
        while True:
            if n == 1:
                return True
            
            n = sum([int(x)**2 for x in str(n)])
            
            if n in temp:
                return False
            
            temp.add(n)
            