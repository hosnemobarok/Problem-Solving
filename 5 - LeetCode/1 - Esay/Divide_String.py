class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        gap = len(s) % k
        mis = k - gap

        total_gap_num = len(s) % k
        mis = k - total_gap_num

        if total_gap_num == 0:
            split_strings = []
            for index in range(0, len(s), k):
                split_strings.append(s[index : index + k])
            return split_strings

        else:
            ss = s + (fill*mis)
            split_strings = []
            for index in range(0, len(ss), k):
                split_strings.append(ss[index : index + k]) 
            return split_strings

        
 
 
"""
s = "abcdefghij"
res = []
for i in range(0, len(s), 2):
    print(s[i: i+2])
   
# Output-
    ab
    cd
    ef
    gh
    ij

"""