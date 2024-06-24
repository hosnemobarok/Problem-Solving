#link : https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longestCommonPrefix = ""
        longestCommonPrefixTepm = ""
        
        lcount = len(strs)
        count = 0
        
        for i in range(200):
            
            if lcount == count:
                count = 0

                if len(set(longestCommonPrefixTepm)) == 1:
                    longestCommonPrefix += longestCommonPrefixTepm[0]

                    longestCommonPrefixTepm = ""
                
                else:
                    return longestCommonPrefix

            for word in strs:
                if len(word) > i:
                    letter = word[i]
                    longestCommonPrefixTepm += letter
                    count += 1
                else:
                    return longestCommonPrefix

        return longestCommonPrefix
