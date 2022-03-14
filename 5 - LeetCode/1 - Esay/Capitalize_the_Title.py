class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        res = title.split()
        
        result = ""
        
        for i in res:
            
            if len(i) == 1 or len(i) == 2:
                result += i.lower() + " "
            else:
                result += i.capitalize() + " "
            
        return result.rstrip()
            
