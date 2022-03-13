from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        perm = permutations([x for x in range(1, n+1)])

        solve = list
        count = 0
        for i in list(perm):

            count += 1
            if count == k:
                solve = i
                break
                
        return "".join(str(x) for x in solve)
