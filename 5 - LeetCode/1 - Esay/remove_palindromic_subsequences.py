# link: https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    
    def is_palindrome(self, string: str) -> bool:
            
        left = 0
        right = len(string)-1
        
        while left < right:
            if string[left] != string[right]:
                return False
            
            else:
                left += 1
                right -= 1
                
        return True
            
            
    def removePalindromeSub(self, s: str) -> int:
        # Best case
        if not s:
            return 0
        
        if self.is_palindrome(s):
            return 1
        else:
            return 2
            
